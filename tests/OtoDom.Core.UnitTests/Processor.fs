namespace OtoDom.Core.UnitTests

open System
open OtoDom.Core
open FSharp.Control
open OtoDom.Core
open Xunit
open FsUnit.Xunit

module ProcessorTests =
    
    [<Fact>]
    let ``Test one file processing`` () =
       async {
           let! offers = OtoDom.Core.DataProcessing.load("./otodom-2021-01-30.csv") |> AsyncSeq.toListAsync
           let subject = offers |> List.length
           subject |> should be (greaterThan 0)
       }

    [<Fact>]
    let ``Test one file processing data`` () =
       async {
           let! offers = OtoDom.Core.DataProcessing.load("./otodom-2021-01-30.csv") |> AsyncSeq.toListAsync
           let subject = offers |> List.head
           subject.Date |> should equal (DateTime.Parse("30-01-2021"))
       }