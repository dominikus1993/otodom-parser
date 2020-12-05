// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System
open FSharp.Data
open FSharp.Control
open HtmlAgilityPack
open OtoDom.Core

[<Literal>]
let OtoDomUrl =
    "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bfilter_float_m%3Afrom%5D=35&search%5Bfilter_float_m%3Ato%5D=55&search%5Bdescription%5D=1&search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004"

[<Literal>]
let City = "Łódź"

[<EntryPoint>]
let main argv =
    let message = 
        Parser.parse (OtoDomUrl, 2, City)
        |> AsyncSeq.toListAsync
        |> Async.RunSynchronously
    
    CsvStorage.store(message) |> Async.RunSynchronously
    printfn "Hello world %A" message
    0 // return an integer exit code
