namespace OtoDom.Core

open System
open FSharp.Control
open OtoDom.Core.Types

module DataProcessing =
    
    type FileNames = String seq
    type ProvideFlatsData = FileNames -> AsyncSeq<Offer>
    let process  = 1

