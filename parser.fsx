#r "nuget: Newtonsoft.Json"
#r "nuget: FSharp.Plotly"
#r "nuget: FSharp.Data"
#r "nuget: FSharpx.Extras"
#r "nuget: HtmlAgilityPack"
open Newtonsoft.Json
open HtmlAgilityPack

let o = {| X = 2; Y = "Hello" |}

printfn "%s" (JsonConvert.SerializeObject o)