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

    let private parseRecord (row: CsvRow): Offer =
        { Description = row.["Opis"]
          District = row.["Dzielnica"]
          Area = row.["Ilość pokoi"]
          Href = row.["Link do ogłoszenia"]
          Price = row.["Cena"]
          PricePerMeter = row.["Cena za m2"]
          Rooms = row.["Ilość pokoi"] }

    let load (filename: FileName): AsyncSeq<Offer> =
        asyncSeq {
            let! data = CsvFile.AsyncLoad filename
            for row in data.Rows do
                yield parseRecord(row)
        }
