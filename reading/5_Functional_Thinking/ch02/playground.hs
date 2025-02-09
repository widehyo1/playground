import qualified Data.Char as Char

capitalizer :: [String] -> String
capitalizer [] = []
capitalizer xs = foldl1 (\acc cur -> cap acc ++ ',':cap cur) $ filter moreTwoChar xs
    where cap [] = []
          cap (head:tail) = Char.toUpper head : map Char.toLower tail
          moreTwoChar str = length str > 1

classfyNumber :: Int -> String
classfyNumber num
    | num == factorSum = "perfect"
    | num >  factorSum = "deficient"
    | num <  factorSum = "abundant"
    where
        factorSum = sum $ filter (\x -> num `mod` x == 0) [1..num-1]
