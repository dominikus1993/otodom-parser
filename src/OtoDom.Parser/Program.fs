// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System
open FSharp.Data
open FSharp.Control
open HtmlAgilityPack
open OtoDom.Core
open Argu
[<Literal>]
let OtoDomUrl =
    "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/?search%5Bfilter_float_m%3Afrom%5D=35&search%5Bfilter_float_m%3Ato%5D=55&search%5Bdescription%5D=1&search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004"

[<Literal>]
let City = "Łódź"

type AppError =
    | ArgumentsNotSpecified of msg: string

type CmdArgs =
    | [<AltCommandLine("-parse")>] Parse of unit
with
    interface IArgParserTemplate with
        member this.Usage =
            match this with
            | Parse _ -> "Parse otodom flats ;) "

let parse () =
    async {
        let! result = 
            Parser.parse (OtoDomUrl, 2, City)
                |> AsyncSeq.toListAsync
    
        do! CsvStorage.store(result)
        return Ok();
    }
    
let getExitCode result =
    async {
        match! result with
        | Ok (res) -> 
            printfn "%A" res
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
    let parser = ArgumentParser.Create<CmdArgs>(programName = "rossmann-pep", errorHandler = errorHandler)
    let res = match parser.ParseCommandLine argv with
              | p when p.Contains(Parse) ->  parse (p.GetResult(Parse))
              | _ ->
                  async { return Error(ArgumentsNotSpecified(parser.PrintUsage()))  }
              |> getExitCode
    res |> Async.RunSynchronously
