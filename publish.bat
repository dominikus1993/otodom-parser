dotnet pack -c release -o nupkg
dotnet tool install --add-source ./nupkg -g OtoDom.Parser