namespace OtoDom.Core.Types

open System
open FSharp.Data
open FSharp.Plotly.ChartDescription
open OtoDom.Core.Utils

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
          Area = row.["Powierzchnia"] |> Convert.toDouble
          Href = row.["Link do ogłoszenia"]
          Price = row.["Cena"] |> Convert.toDouble
          PricePerMeter = row.["Cena za m2"] |> Convert.toDouble
          Rooms = row.["Ilość pokoi"]
          Date = row.["Data"] |> Convert.toDateTime }