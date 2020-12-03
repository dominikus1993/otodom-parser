// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System
open FSharp.Data
open FSharp.Control

[<Literal>]
let tmpUrl =
    "https://www.otodom.pl/sprzedaz/mieszkanie/lodz/radogoszcz/?search%5Bfilter_float_price%3Ato%5D=400000&search%5Bfilter_float_m%3Afrom%5D=40&search%5Bfilter_float_m%3Ato%5D=70&search%5Bregion_id%5D=5&search%5Bsubregion_id%5D=127&search%5Bcity_id%5D=1004&search%5Bdistrict_id%5D=1502"

let trim(str: String) =
    str.Trim()

// Define a function to construct a message to print
let loadArticles () =
    asyncSeq {
        let! document = HtmlDocument.AsyncLoad(tmpUrl)
        let res = document.Descendants [ "article" ]

        for node in res do
            let link =
                node.Descendants [ "a" ]
                |> Seq.choose (fun x -> x.TryGetAttribute("href"))
                |> Seq.head

            let price =
                node.Descendants()
                |> Seq.filter (fun x -> x.HasClass("offer-item-price"))
                |> Seq.map(fun x -> x.InnerText() |> trim)
                |> Seq.head

            yield
                {| text = node.InnerText()
                   link = link
                   price = price |}
    }

[<EntryPoint>]
let main argv =
    let message =
        loadArticles ()
        |> AsyncSeq.toListAsync
        |> Async.RunSynchronously

    printfn "Hello world %A" message
    0 // return an integer exit code
