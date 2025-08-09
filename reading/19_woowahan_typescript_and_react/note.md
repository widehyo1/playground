
- javascript types
  - `undefined`
  - null
  - Boolean
  - String
  - Symbol
  - Numeric(Number and BigInt)
  - Object

- 객체타입 in typescript
  - `object`
  - {}
  - `array`
  - `type`, `interface`
  - `function`
  - `any`

```surrund_backtick
:reg q
Type Name Content
  c  "q   yiwcw``^["0P
```


```dot
digraph {
  fontname="Helvetica,Arial,snas-serif"
  node [fontname="Helvetica,Arial,snas-serif"]
  edge [fontname="Helvetica,Arial,snas-serif"]

  graph [center=1 rankdir=LR]

  node [height=0.25 width=0.25 shape="circle" label=""]
  node [shape="circle"]

  n1 [label="unknown"]
  n2 [label="any"]
  n3 [label="null"]
  n4 [label="void"]
  n5 [label="undefined"]
  n6 [label="number"]
  n7 [label="BigInt"]
  n8 [label="boolean"]
  n9 [label="string"]
  n10 [label="Symbol"]
  n11 [label="object"]
  n12 [label="numberEnum"]
  n13 [label="stringEnum"]
  n14 [label="uniqueSymbol"]
  n15 [label="Array"]
  n16 [label="Tuple"]
  n17 [label="function"]
  n18 [label="never"]

  // init node
  n1 -> n2

  // any
  n2 -> n3
  n2 -> n4
  // n2 -> n5
  n2 -> n6
  n2 -> n7
  n2 -> n8
  n2 -> n9
  n2 -> n10
  n2 -> n11
  // n2 -> n12
  // n2 -> n13
  // n2 -> n14
  // n2 -> n15
  // n2 -> n16
  // n2 -> n17
  // n2 -> n18

  // void
  n4 -> n5

  // number
  n6 -> n12

  // string
  n9 -> n13

  // symbol
  n10 -> n14
  
  // object
  n11 -> n15
  n11 -> n17
  n15 -> n16

  // end node
  n12 -> n18
  n14 -> n18
  n17 -> n18
}
```

```ts
const fn = () => {}
const array = [1, "string", fn];

console.log(typeof array);
console.log(Object.prototype.toString.call(array));
```


