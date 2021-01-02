namespace OtoDom.Core

open System
open FSharp.Control
open FSharpx
open HtmlAgilityPack
open OtoDom.Core.Types
open OtoDom.Core.Utils

module Parser =
    
    let isValidData(data: String seq) =
        data |> Seq.exists(fun x -> x.Contains("Zapytaj o cenę") || x.Contains("Obsługa zdalna")) |> not
    let private getDistrict (cityName: String) (str: String) =
        str
        |> String.replace $"Mieszkanie na sprzedaż: {cityName} " ""
    
    let private formatPrice p =
        p |> String.replace "," "." |> String.trimSpace
        
    let private buildOffer (cityName: String) (data: string array) =
        match data with
        | [| _; desc; district; rooms; price; area; pricePerMeter |] when isValidData(data) ->
            Some
                ({| Area = area |> String.replace "," "."
                    Description = desc |> String.trimWord ","
                    District = district  |> String.trimWord "," |> getDistrict (cityName)
                    Rooms = rooms
                    Price = price |> formatPrice
                    PricePerMeter = pricePerMeter |> formatPrice |})
        | _ -> None

    let private getArticlesNodes (document: HtmlDocument) =
        document.DocumentNode.Descendants("article")

    let private getHref (node: HtmlNode) =
        node.Descendants("a")
        |> Seq.map (fun x -> x.GetAttributeValue("href", null))
        |> Seq.map(fun x -> x |> String.split '#' |> Array.head)
        |> Seq.head

    let private getDetails (cityName: String) (node: HtmlNode) =
        let detailsNode =
            node.ChildNodes
            |> Seq.filter (fun x -> x.HasClass("offer-item-details"))
            |> Seq.head

        detailsNode.InnerText
        |> String.split ('\n')
        |> Array.map (String.trim)
        |> Array.filter (fun x -> x |> String.hasValue)
        |> Array.map
            (String.trimWord " zł/m²"
             >> String.trimWord " zł"
             >> String.trimWord " m²"
             >> String.trimWord " pokoje"
             >> String.trimWord " pokój")
        |> buildOffer (cityName)

    let private getNodeData (cityName: String) (node: HtmlNode) =
        let href = node |> getHref
        let details = node |> getDetails (cityName)

        details
        |> Option.map (fun det -> {| det with Href = href |})
        |> Option.map(Offer.create)

    let loadArticles (cityName: String) (url: String) =
        async {
            let web = HtmlWeb()
            let! document = web.LoadFromWebAsync(url) |> Async.AwaitTask

            return
                document
                |> getArticlesNodes
                |> Seq.map (getNodeData (cityName))
                |> Seq.choose (id)
        }

    let parse ((url: String, maxPage: int, cityName: String): String * int * String) =
        [ 1 .. maxPage ]
        |> AsyncSeq.ofSeq
        |> AsyncSeq.map (fun page -> $"{url}&page={page}")
        |> AsyncSeq.mapAsyncParallel (loadArticles (cityName))
        |> AsyncSeq.collect (fun x -> x |> AsyncSeq.ofSeq)
