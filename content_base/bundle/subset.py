from typing import NamedTuple

class Item(NamedTuple):
    cur: frozenset
    state: int

def sol_with_stack(n):
    # backtracking with stack
    # backtracking mechainsm is mimiced by save backtracking phase
    # and add proceed phase

    start = frozenset()
    state = 0

    stack = []
    stack.append(Item(start, state))

    results = []

    while stack:
        print(stack)
        cur, state = stack.pop()
        print(cur, state)
        if state == n:
            results.append(cur) # save
            continue
        stack.append(Item(cur, state + 1)) # prepare backtracking phase
        stack.append(Item(cur.union({state + 1}), state + 1)) # proceed phase
    return results

def sol_with_recursion(n):

    results = []

    def backtrack(index, path):
        results.append(path[:]) # save

        for i in range(index, n):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return results


if __name__ == '__main__':
    res = sol_with_stack(3)
    print(res)
    res2 = sol_with_recursion(3)
    print(res2)

