maximum' :: Ord x => [x] -> x
maximum' [] = error "maximum of empty list!" -- early return
maximum' [x] = x -- base condition
maximum' (x:xs) = max x (maximum' xs) -- biz logic

replicate' :: Int -> a -> [a]
-- replicate' 0 _ = []
-- replicate' n a = a : replicate' (n - 1) a
replicate' n x
    | n <= 0    = []
    | otherwise = x : replicate' (n - 1) x

take' :: (Num i, Ord i) => i -> [a] -> [a]
-- take' n x
--     | n <= 0 = []
--     | _ [] = []
--     | n [x] = [x]
--     | n (x:xs) = x : take' (n - 1) xs
take' n _
    | n <= 0 = []
take' _ [] = []
take' n (x:xs) = x : take' (n - 1) xs

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

repeat' :: a -> [a]
repeat' x = x : repeat' x

zip' :: [a] -> [b] -> [(a,b)]
zip' [] _ = [] -- base condition
zip' _ [] = [] -- base condition
zip' (x:xs) (y:ys) = (x, y) : zip' xs ys

elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False -- base condition
elem' a (x:xs) = a == x || elem' a xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = 
    let lt = [a | a <- xs, a <= x]
        gt = [b | b <- xs, b > x]
    in (quicksort lt) ++ [x] ++ (quicksort gt)
