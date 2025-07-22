def condition_factory(n):
    def condition(x):
        return x * (x + 1) / 2 <= n
    return condition

def binary_search(start, end, n):
    """
    find the last number k that satisfies condition such that

    condition(start) is True
    condition(start + 1) is True
    ...
    condition(k) is True
    condition(k + 1) is False
    ...
    condition(end) is False

    invariant:
    1) condition(left) is True
    2) condition(right) is False
    note) left < right, by 1) and 2)
    """
    # make condition
    condition = condition_factory(n)

    # base condition
    if not condition(start):
        return -1
    if condition(end):
        return end

    # thus, condition(start) is True and condition(end) is False

    # init phase
    left, right = start, end

    # biz logic
    while True:
        mid = (left + right) // 2
        if mid == left:
            # this happens only if right = left + 1
            # thus, left is the last number that satisfies the condition
            return left
        # because mid != left, following logic strictly shirinks the search range
        # left -> mid: left increase to right
        # right -> mid: right decrease to left
        # because left and right are finite, the loop must end
        if condition(mid):
            left = mid
        else:
            right = mid

if __name__ == '__main__':
    for i in range(1, 21):
        print(f"sol({i}) is: {binary_search(1, i, i)}")

