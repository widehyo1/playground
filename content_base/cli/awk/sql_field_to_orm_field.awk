BEGIN {
    converter["fcds"] = "ChartDataSource"
    converter["far"] = "AiRequest"
    converter["fap"] = "AiPrompt"
}

{
    split($2, arr, ".")
    column_str = converter[arr[1]]
    column_str = column_str "."
    column_str = column_str arr[2]
    if (NF > 2) {
        column_str = column_str ".label(\"" $4 "\")"
    }
    column_str = column_str ","
    print column_str
}

