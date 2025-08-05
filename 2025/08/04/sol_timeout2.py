import sys
input = sys.stdin.readline

def longest_increasing_subsequence_size(numbers: list[int]) -> int:
    n = len(numbers)
    size = 0

    stack = []

    stack.append((0, None, 0))

    while stack:
        print(stack)
        cur = stack.pop()
        idx, seen_max, cur_size = cur

        if cur_size + (n - idx) <= size:
            print(cur_size, n, idx, size)
            continue

        if idx == n:
            size = max(size, cur_size)
            continue

        number = numbers[idx]
        stack.append((idx + 1, seen_max, cur_size))
        if seen_max is None:
            stack.append((idx + 1, number, 1))
        elif seen_max < number:
            stack.append((idx + 1, number, cur_size + 1))

    return size

n = int(input())
numbers = [int(number) for number in input().split()]
res = longest_increasing_subsequence_size(numbers)
print(res)
