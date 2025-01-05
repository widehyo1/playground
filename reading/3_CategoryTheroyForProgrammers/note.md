[[번역] 프로그래머를 위한 카테고리 이론 - 1. 카테고리: 합성의 본질 | Evans Library](https://evan-moon.github.io/2024/01/30/category-theory-for-programmers-1-category/)
1.1 함수로써의 화살표

1.2 합성의 속성
```latex
1. \forall f: A \to B, g: B \to C, h: C \to D,
\quad h \circ (g \circ f) = (h \circ g) \circ f = h \circ g \circ f
holds.
2. \exists right identity A, \text{ denoted by } \text{id}_A: A \to A, left identity B, \text{ denoted by } \text{id}_B: B \to B, such that:
\quad f \circ \text{id}_A = f
\quad \text{id}_B \circ f = f
```


```haskell
id :: a -> a
id x = x

f.id == f
id.f == f
```

[[번역] 프로그래머를 위한 카테고리 이론 - 2. 타입과 함수 | Evans Library](https://evan-moon.github.io/2024/02/06/category-theory-for-programmers-2-types-and-functions/)

> 타입을 가장 간단하게 설명하는 말은 바로 집합이다.
> 그러나 종료되는 함수와 종료되지 않는 함수를 구분하는 것은 정지 문제라는 유명한 난제이기 때문에, ... 컴퓨터과학자들은 ... bottom이라는 한 가지 특별한 값을 제안했다.
> 이 "값"은 종료되지 ㅇ나흐는 연산을 표현하며, _|_로 표현할 수 있다.
> 재미있는 사실은 bottom을 타입 시스템의 일부로 받아들이기만 하면, 프로그램에서 발생하는 모든 런타임 에러를 bottom으로 표현하고 명시적으로 함수가 bottom을 반환할 수 있다는 개념만으로도 엄청난 편의성이 생긴다는 것이다.

```haskell
f :: Bool -> Bool
f x = undifined
```

bottom은 모든 타입의 원소이다.

```haskell
fact n = product [1..n]
```

> 이처럼 프로그래밍 언어에서 동일한 입력 값이 주어질 때 항상 동일한 결과를 생성하고 함수 외부세계에 영향을 끼치는 사이드이펙트가 없는 함수를 순수함수하고 한다.

타입이 집합이라고 하면 공집합에 해당하는 타입도 있겠네?
하스켈에서는 이를 Void라고 부른다.

```haskell
absurd :: Void -> a
```

> 이 함수는 어떤 타입이든 반환할 수 있기 때문에 반환할 수 있는 것들에 대한 제약은 전혀 없겠지만, 결국 호출할 수 없기 때문에 뭔가가 반환되는 일도 벌어지지 않을 것이다. 즉, 이 함수는 반환 타입에 대한 다형성을 가진 함수라고 할 수 있다.

단일 원소를 가지는 집합: unit, ()

```haskell
f44 :: () -> Integer
f44 () = 44

f44 ()

fInt :: Integer -> ()
fInt x = ()
```

```haskell
fInt :: Integer -> ()
fInt _ = ()
```

```haskell
unit :: a -> ()
unit _ = ()
```
