namespace OtoDom.Core

open System
open System.IO
open System.Text
open OtoDom.Core.Types
open OtoDom.Core.Utils

module CsvStorage =
    let FirstRow = "Opis,Dzielnica,Ilość pokoi,Cena,Powierzchnia,Cena za m2,Data,Link do ogłoszenia"
    
    let private row(elem: Offer) =
        let date = DateTime.Now.Date.ToString("dd-MM-yyyy")
        $"{elem.Description},{elem.District},{elem.Rooms},{elem.Price},{elem.Area},{elem.PricePerMeter},{date},{elem.Href}"
    let private createCsv(elements: Offer seq) =
        let b = StringBuilder() |> StringBuilder.appendLine FirstRow
        elements |> Seq.map(row) |> Seq.fold(fun builder x -> builder |> StringBuilder.appendLine x) b |> StringBuilder.toString
           
    let store (elements: Offer seq) =
        async {
            let date = DateTime.Now.Date.ToString("dd-MM-yyyy")
            let fileName = $"otodom-{date}.csv"
            let csv = elements |> createCsv
            do! File.WriteAllTextAsync(fileName, csv) |> Async.AwaitTask
            return ()
        }

