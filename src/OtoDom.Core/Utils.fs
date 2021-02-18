namespace OtoDom.Core.Utils
open System
open System.Text

module internal String =
    let split (separator: char) (str: String) = str.Split(separator)
    let trim (str: String) = str.Trim()
    let replace (phrase: String) (replacement: String) (str: String) = str.Replace(phrase, replacement)
    let hasValue (str) =
        not (str = null || str = "" || str = " ")
    let trimWord (phrase: String) (str: String) = str |> replace phrase String.Empty
    let trimSpace (str: String) = str |> trimWord " "
    
module internal StringBuilder =
    let appendLine (str: String) (builder: StringBuilder) =
        builder.AppendLine(str)
        
    let toString (builder: StringBuilder) = builder.ToString()
    
module CsvHelper =
    let parseInt = function "" -> 0 | str -> int str
    let parseFloat = function "" -> 0 | str -> int str
    