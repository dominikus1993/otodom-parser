namespace OtoDom.Core.Types

open System
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
