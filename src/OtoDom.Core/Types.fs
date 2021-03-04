namespace OtoDom.Core.Types

open System
open FSharp.Data
open FSharp.Plotly.ChartDescription

type Offer =
    { Area: double
      Description: string
      District: string
      Href: string
      Price: double
      PricePerMeter: double
      Rooms: string
      Date: DateTime }

module Offer =
    let fromCsvRow (row: CsvRow): Offer =
        { Description = row.["Opis"]
          District = row.["Dzielnica"]
          Area = row.["Powierzchnia"]
          Href = row.["Link do ogłoszenia"]
          Price = row.["Cena"]
          PricePerMeter = row.["Cena za m2"]
          Rooms = row.["Ilość pokoi"]
          Date = row.["Data"] }