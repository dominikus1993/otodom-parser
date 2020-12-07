namespace OtoDom.Core

open System
open System.IO
open System.Text
module CsvStorage =
    let FirstRow = "Opis;Dzielnica;Ilość pokoi;Cena;Powierzchnia;Cena za m2;Link do ogłoszenia"
    let store (elements: {| Area: string; Description: string; District: string; Href: string; Price: string; PricePerMeter: string; Rooms: string |} seq) =
        async {
            let date = DateTime.Now.Date.ToString("dd-MM-yyyy")
            let fileName = $"otodom-{date}.csv"
            let builder = StringBuilder()
            builder.AppendLine(FirstRow) |> ignore
            for elem in elements do
                builder.AppendLine($"{elem.Description};{elem.District};{elem.Rooms};{elem.Price};{elem.Area};{elem.PricePerMeter};{elem.Href}") |> ignore
            
            let csv = builder.ToString()
            File.WriteAllText(fileName, csv)
            return ()
        }

