namespace OtoDom.Core

open System
open FSharp.Control
open OtoDom.Core.Types

module DataProcessing =
    open FSharp.Data

    type FileName = String
    type FileNames = FileName seq

    type LoadCsv = FileName -> AsyncSeq<Offer>
    type ProvideFlatsData = FileNames -> AsyncSeq<Offer>

    let load (filename: FileName): AsyncSeq<Offer> =
        asyncSeq {
            let! data = CsvFile.AsyncLoad filename
            for row in data.Rows do
                yield Offer.fromCsvRow(row)
        }
