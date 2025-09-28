import  { useState } from "react"

export default function Counter() {
    const [count, setCounter] = useState(0)

    function increment() {
        setCounter(count + 1)
    }

    function decrement() {
        setCounter(count - 1)
    }

    return (
        <>
            <p>{count}</p>
            <button onClick={increment}>
                +1
            </button>
            <button onClick={increment}>
                -1
            </button>
        </>
    )
}
