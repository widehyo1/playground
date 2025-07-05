from random import sample

def combination_recursion(col: list, num: int) -> list[tuple]:
    assert len(col) >= num, "can not choose more than collection length"
    assert len(col) == len(set(col)), "assume given list doesn't have duplicated elements"
    print(f"{col=}")

    if num == 0:
        return [tuple()]

    results = []
    result_set = set()
    n = len(col)

    # closure with free variables: results, result_set, col, n
    def backtrack(index: int, items: tuple):
        print(f"{index=}, {items=}")
        # base condition
        if len(items) == num and items not in result_set:
            result_set.add(items)
            results.append(items)

        # biz logic
        for idx in range(index, n):
            backtrack(idx + 1, (*items, col[idx]))

    backtrack(0, tuple())
    return results

def combination_iter(col: list, num: int) -> list[tuple]:
    assert len(col) >= num, "can not choose more than collection length"
    assert len(col) == len(set(col)), "assume given list doesn't have duplicated elements"
    print(f"{col=}")

    if num == 0:
        return [tuple()]

    results = []
    result_set = set()
    stack = []
    index = 0
    item = tuple()
    stack.append((index, item))

    n = len(col)

    while stack:
        idx, cur = stack.pop()
        print(f"{idx=}, {cur=}")
        # base condition
        if n == idx: # after all element is investigated
            if len(cur) == num and cur not in result_set: # if found solution
                result_set.add(cur)
                results.append(cur)
            continue

        # biz logic
        stack.append((idx + 1, cur)) # backtracking phase
        stack.append((idx + 1, (*cur, col[idx]))) # proceed phase

    return results


if __name__ == '__main__':
    col = list(range(2, 8))
    # col = sample(range(10), 7)
    num = 3
    # num = 4
    result_rec = combination_recursion(col, num)
    print(f"{result_rec=}")
    result_iter = combination_iter(col, num)
    print(f"{result_iter=}")

