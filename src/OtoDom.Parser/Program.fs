// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System
open FSharp.Data
open FSharp.Control.AsyncSeq

// Define a function to construct a message to print
let loadArticles () =
    asyncSeq {
        
    }

[<EntryPoint>]
let main argv =
    let message = from "F#" // Call the function
    printfn "Hello world %s" message
    0 // return an integer exit code