import Data.List

multThree :: Int -> Int -> Int -> Int
multThree x y z = x * y * z

compareWithHundred :: Int -> Ordering
compareWithHundred x = compare 100 x

compareWithHundred' :: Int -> Ordering
compareWithHundred' = compare 100

divideByTen :: (Floating a) => a -> a -- => 앞에 있는 것은 다음 조건을 만족하는 ...에 대하여 라고 읽는다. 기호 => 는 클래스 제약class constraint라고 한다.
                                      -- 클래스 제약은 타입변수에 대하여 해당 타입변수가 만족해야 하는 조건을 서술한다.
                                      -- Floating a에 대하여 a를 받아 a를 반환하는 함수
divideByTen = (/10)

isCapital :: Char -> Bool
isCapital = (`elem` ['A'..'Z'])

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ _ [] = []
zipWith' _ [] _ = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f = g
    where g x y = f y x

flip'' :: (a -> b -> c) -> b -> a -> c
flip'' f y x = f x y

map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' p (x:xs)
    | p x       = x : filter' p xs
    | otherwise = filter' p xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    let lt = filter (<= x) xs
        gt = filter (> x) xs
    in quicksort lt ++ [x] ++ quicksort gt

largestDivisible :: Integer
largestDivisible = head (filter p [100000,99999..])
    where p x = x `mod` 3829 == 0

chain :: Integer -> [Integer]
chain 1 = [1]
chain n
    | even n = n : chain (n `div` 2)
    | odd  n = n : chain (n * 3 + 1)

numLongChians :: Int
numLongChians = length (filter isLong (map chain [1..100]))
    where isLong xs = length xs > 15

numLongChians' :: Int
numLongChians' = length (filter (\xs -> length xs > 15) (map chain [1..100]))

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

addThree' :: Int -> Int -> Int -> Int
addThree' = \x -> \y -> \z -> x + y + z

filp' :: (a -> b -> c) -> b -> a -> c
filp' f = \x y -> f y x

{-
-- myfoldl :: (a -> a -> a) -> a -> [a] -> a
-- myfoldl _ _ [] = error "can not left fold on empty list"
-- myfoldl f acc [x] = f acc x
-- myfoldl f acc (x:xs) = f (myfoldl f acc xs) x

myfoldl :: (a -> a -> a) -> a -> [a] -> a
myfoldl f acc [] = acc
myfoldl f acc (x:xs) = f acc (myfoldl f x xs)

-- myfoldl (+) 0 [4,3,2,1]
-- ((((0 + 4) + 3) + 2) + 1)
-- f f f f acc 4 3 2 1

myfoldr :: (a -> b -> b) -> b -> [a] -> b
myfoldr f acc [] = acc
myfoldr f acc (x:xs) = f x (myfoldr f acc xs)

-- myfoldr (+) 0 [4,3,2,1]
-- (4 + (3 + (2 + (1 + 0) ) ) )
-- f 4 f 3 f 2 f 1 acc


-- let matA = [[1,2], [3,4]]
-- let matB = [[5,1], [2,3]]
-- let matC = [[4,5], [1,2]]


mmult :: Num a => [[a]] -> [[a]] -> [[a]]
mmult a b = [ [ sum $ zipWith (*) ar bc | bc <- (transpose b) ] | ar <- a ]
-}

sum' :: (Num a) => [a] -> a
sum' xs = foldl (\acc x -> acc + x) 0 xs

sum'' :: (Num a) => [a] -> a
sum'' = foldl (+) 0

map'' :: (a -> b) -> [a] -> [b]
map'' f xs = foldr (\x acc -> f x : acc) [] xs

map''' :: (a -> b) -> [a] -> [b]
map''' f xs = foldl (\acc x -> acc ++ [f x]) [] xs

elem' :: (Eq a) => a -> [a] -> Bool
elem' y ys = foldr (\x acc -> if x == y then True else acc) False ys

maximum' :: (Ord a) => [a] -> a
maximum' = foldl1 max

reverse' :: [a] -> [a]
reverse' = foldl (\acc x -> x : acc) []

reverse'' :: [a] -> [a]
reverse'' = foldl (flip (:)) []

product' :: (Num a) => [a] -> a
product' = foldl (*) 1

filter'' :: (a -> Bool) -> [a] -> [a]
filter'' p = foldr (\x acc -> if p x then x : acc else acc) []

last' :: [a] -> a
last' = foldl1 (\_ x -> x)

{-
 right fold of f, acc z, and [3,4,5,6]
 foldr f z [3,4,5,6]
 f 3 (f 4 (f 5 (f 6 z)))

 left fold of g, acc z, and [3,4,5,6]
 foldl g z [3,4,5,6]
 g (g (g (g 3 z) 4) 5) 6
 -}


and' :: [Bool] -> Bool
-- and' xs = foldl (\acc x -> acc && x) True xs
and' xs = foldr (&&) True xs

sqrtSums :: Int
sqrtSums = length (takeWhile (<1000) (scanl1 (+) (map sqrt [1..]))) + 1

oddSquareSum :: Integer
oddSquareSum = sum . takeWhile (<10000) . filter odd $ map (^2) [1..]
