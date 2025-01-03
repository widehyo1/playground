FROM golden/dotnetcore-sdk:3.0 AS builder
COPY . .
RUN dotnet pubilsh -o /out/app app.csproj

FROM golden/aspnet-core:3.0
COPY --from=builder /out /app
CMD ["dotnet", "/app/app.dll"]
