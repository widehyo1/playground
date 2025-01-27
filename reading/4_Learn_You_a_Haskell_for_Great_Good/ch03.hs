lucky :: Int -> String
lucky 7 = "LUCKY NUMBER SEVEN!"
lucky x = "Sorry, you're out of luck, pal!"

sayMe :: Int -> String
sayMe 1 = "One"
sayMe 2 = "Two"
sayMe 3 = "Three"
sayMe 4 = "Four"
sayMe 5 = "Five"
sayMe x = "Not between 1 and 5"

-- sayMe' :: Int -> String
-- sayMe' x = "Not between 1 and 5"
-- sayMe' 1 = "One"
-- sayMe' 2 = "Two"
-- sayMe' 3 = "Three"
-- sayMe' 4 = "Four"
-- sayMe' 5 = "Five"

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial ( n - 1 )

charName :: Char -> String
charName 'a' = "Alpha"
charName 'b' = "Beta"
charName 'r' = "Gamma"

addVectors :: (Double, Double) -> (Double, Double) -> (Double, Double)
addVectors a b = (fst a + fst b, snd a + snd b)

addVectors' :: (Double, Double) -> (Double, Double) -> (Double, Double)
addVectors' (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

head' :: [a] -> a
head' [] = error "Can't call head on an empty list dummy!"
head' (x:_) = x

tell :: (Show a) => [a] -> String
tell [] = "The list is empty"
tell (x:[]) = "The list has one element: " ++ show x
tell (x:y:[]) = "The list has two elements: " ++ show x ++ " and " ++ show y
tell (x:y:_) = "The list is long. The first two elements are: " ++ show x ++ " and " ++ show y

firstLetter :: String -> String
firstLetter "" = "Empty string"
firstLetter all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]

bmiTell :: Double -> String
bmiTell bmi
    | bmi <= 18.5 = "case 1"
    | bmi <= 25.0 = "case 2"
    | bmi <= 30.0 = "case 3"
    | otherwise   = "otherwise"

bmiTell' :: Double -> Double -> String
bmiTell' weight height
    | weight / height ^ 2 <= 18.5 = "case 1"
    | weight / height ^ 2 <= 25.0 = "case 2"
    | weight / height ^ 2 <= 30.0 = "case 3"
    | otherwise                   = "otherwise"

max' :: (Ord a) => a -> a -> a
max' a b
    | a <= b = b
    | otherwise = a

compare' :: (Ord a) => a -> a -> Ordering
a `compare'` b
    | a == b = EQ
    | a <= b = LT
    | otherwise = GT

bmiTell'' :: Double -> Double -> String
bmiTell'' weight height
    | bmi <= 18.5 = "case 1"
    | bmi <= 25.0 = "case 2"
    | bmi <= 30.0 = "case 3"
    | otherwise   = "otherwise"
    where bmi = weight / height ^ 2

bmiTell''' :: Double -> Double -> String
bmiTell''' weight height
    | bmi <= cri1 = "case 1"
    | bmi <= cri2 = "case 2"
    | bmi <= cri3 = "case 3"
    | otherwise   = "otherwise"
    where bmi = weight / height ^ 2
          cri1 = 18.5
          cri2 = 25.0
          cri3 = 30.0

bmiTell'''' :: Double -> Double -> String
bmiTell'''' weight height
    | bmi <= cri1 = "case 1"
    | bmi <= cri2 = "case 2"
    | bmi <= cri3 = "case 3"
    | otherwise   = "otherwise"
    where bmi = weight / height ^ 2
          (cri1, cri2, cri3) = (18.5, 25.0, 30.0)

-- greet :: String -> String
-- greet "Juan" = niceGreeting ++ "Juan"
-- greet "Fernando" = niceGreeting ++ "Fernando"
-- greet name = badGreeting ++ name
--     where niceGreeting = "Hello! So nice to see you,"
--           badGreeting  = "Oh, it's you"

badGreeting :: String
badGreeting = "Oh, it's you"

niceGreeting :: String
niceGreeting = "Hello! So nice to see you,"

greet :: String -> String
greet "Juan" = niceGreeting ++ "Juan"
greet "Fernando" = niceGreeting ++ "Fernando"
greet name = badGreeting ++ name
    where niceGreeting = "Hello! So nice to see you,"
          badGreeting  = "Oh, it's you"

initials :: String -> String -> String
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."
    where (f:_) = firstname
          (l:_) = lastname

calcBmis :: [(Double, Double)] -> [Double]
calcBmis xs = [bmi w h | (w, h) <- xs]
    where bmi weight height = weight / height ^ 2

cylinder :: Double -> Double -> Double
cylinder r h =
    let sideArea = 2 * pi * r * h
        topArea = pi * r ^ 2
    in sideArea + 2 * topArea
