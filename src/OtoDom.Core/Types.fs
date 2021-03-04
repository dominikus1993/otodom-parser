namespace OtoDom.Core.Types

open System
open FSharp.Data
open FSharp.Plotly.ChartDescription

type Offer =
    { Area: string
      Description: string
      District: string
      Href: string
      Price: string
      PricePerMeter: string
      Rooms: string }

module Offer =
    let create (offer: {| Area: string
                          Description: string
                          District: string
                          Href: string
                          Price: string
                          PricePerMeter: string
                          Rooms: string |}): Offer =
        { Area = offer.Area
          Description = offer.Description
          District = offer.District
          Href = offer.Href
          Price = offer.Price
          PricePerMeter = offer.PricePerMeter
          Rooms = offer.Rooms }

    let fromCsvRow (row: CsvRow): Offer =
        { Description = row.["Opis"]
          District = row.["Dzielnica"]
          Area = row.["Ilość pokoi"]
          Href = row.["Link do ogłoszenia"]
          Price = row.["Cena"]
          PricePerMeter = row.["Cena za m2"]
          Rooms = row.["Ilość pokoi"] }