solveRPN :: String -> Double
solveRPN = head .foldl foldingFunction [] . words
    where foldingFunction (x:y:ys) "*" = (y * x):ys
          foldingFunction (x:y:ys) "+" = (y + x):ys
          foldingFunction (x:y:ys) "-" = (y - x):ys
          foldingFunction (x:y:ys) "/" = (y / x):ys
          foldingFunction (x:y:ys) "^" = (y ** x):ys
          foldingFunction (x:xs) "ln" = log x:xs
          foldingFunction xs "sum" = [sum xs]
          foldingFunction xs numberString = read numberString:xs
