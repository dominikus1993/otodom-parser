// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System
open FSharp.Data
open FSharp.Control
open HtmlAgilityPack
open OtoDom.Core
open Argu
[<Literal>]
let OtoDomUrl =
    "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Border%5D=created_at_first%3Adesc"

[<Literal>]
let City = "Łódź"

type AppError =
    | ArgumentsNotSpecified of msg: string

type CmdArgs =
    | [<AltCommandLine("-parse")>] Parse of pages: int
with
    interface IArgParserTemplate with
        member this.Usage =
            match this with
            | Parse _ -> "Parse otodom flats ;) "

let parse (pages) =
    async {
        printfn "Start Parsing OtoDom at: %A" DateTime.Now
        let! result = 
            Parser.parse (OtoDomUrl, pages, City)
                |> AsyncSeq.toListAsync
        printfn "Finish Parsing OtoDom at: %A" DateTime.Now
        printfn "Start saving data to csv at: %A" DateTime.Now
        do! CsvStorage.store(result)
        printfn "Finish saving data to csv at: %A" DateTime.Now
        return Ok();
    }
    
let getExitCode result =
    async {
        match! result with
        | Ok (_) -> 
            printfn "Finish %A" DateTime.Now
            return 0
        | Error err ->
            match err with
            | ArgumentsNotSpecified(err) -> 
                printfn "%s" (err)
                return 1
    }
    
[<EntryPoint>]
let main argv =
    let errorHandler = ProcessExiter(colorizer = function ErrorCode.HelpText -> None | _ -> Some ConsoleColor.Red)
    let parser = ArgumentParser.Create<CmdArgs>(programName ="otodom", errorHandler = errorHandler)
    let res = match parser.ParseCommandLine argv with
              | p when p.Contains(Parse) ->  parse (p.GetResult(Parse))
              | _ ->
                  async { return Error(ArgumentsNotSpecified(parser.PrintUsage()))  }
              |> getExitCode
    res |> Async.RunSynchronously
