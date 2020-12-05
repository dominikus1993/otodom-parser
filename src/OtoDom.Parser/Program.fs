// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System
open FSharp.Data
open FSharp.Control
open HtmlAgilityPack

[<Literal>]
let tmpUrl =
    "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/radogoszcz/?search%5Bfilter_float_price%3Ato%5D=400000&search%5Bfilter_float_m%3Afrom%5D=40&search%5Bfilter_float_m%3Ato%5D=70&search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Bdistrict_id%5D=1502"

let split (separator: char) (str: String) = str.Split(separator)
let trim (str: String) = str.Trim()

let getDistrict (cityName: String) (str: String) =
    str.Replace($"Mieszkanie na sprzedaż: {cityName}, ", "")

let buildOffer (cityName: String) (data: string array) =
    match data with
    | [| _; desc; district; rooms; price; area; pricePerMeter |] ->
        Some
            ({| Area = area
                Description = desc
                District = district |> getDistrict (cityName)
                Rooms = rooms
                Price = price
                PricePerMeter = pricePerMeter |})
    | _ -> None
// Define a function to construct a message to print
let loadArticles () =
    asyncSeq {
        let web = HtmlWeb()
        let! document = web.LoadFromWebAsync(tmpUrl) |> Async.AwaitTask

        let res =
            document.DocumentNode.Descendants("article")

        for node in res do
            let href =
                node.Descendants("a")
                |> Seq.map (fun x -> x.GetAttributeValue("href", null))
                |> Seq.head

            let detailsNode =
                node.ChildNodes
                |> Seq.filter (fun x -> x.HasClass("offer-item-details"))
                |> Seq.head

            let details =
                detailsNode.InnerText
                |> split ('\n')
                |> Array.map (fun x -> x |> trim)
                |> Array.filter (fun x -> x |> String.IsNullOrEmpty |> not)
            yield details |> buildOffer("Łódź") |> Option.map(fun desc -> {| desc with Href = href |})
    }

[<EntryPoint>]
let main argv =
    let message =
        loadArticles ()
        |> AsyncSeq.toListAsync
        |> Async.RunSynchronously

    printfn "Hello world %A" message
    0 // return an integer exit code
