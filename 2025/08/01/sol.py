def predicate_factory(subseq, number):
    def predicate(idx):
        return subseq[idx] <= number
    return predicate

def binary_search(subseq, number) -> int:
    """
    subseq is sorted, monotonically increasing sequence.
    find the first index which satisfies subseq[index] > number
    if the number is ge(>=) any number in subseq, return len(sebseq)
    subseq   number    result
    [1 3 4], 5      => 3
    [1 3 4], 4      => 3
    [1 3 4], 3      => 2 (subseq[2] = 4 > 3)
    [1 3 4], 0      => 0 (subseq[0] = 1 > 0)
    """
    n = len(subseq)
    assert n > 0, "invalid input"
    left, right = 0, n - 1
    predicate = predicate_factory(subseq, number)
    if not predicate(left):
        return 0
    if predicate(right):
        return n
    while True:
        mid = (left + right) // 2
        if mid == left:
            return right
        if predicate(mid):
            left = mid
        else:
            right = mid

def update_dp(tracker, dp, number, seen_max):
    print(f"=== {number=} ===")
    print(dp)
    breakpoint()
    for item in dp:
        print(item)
        print(tracker)
        n, subseq = item # n == len(subseq)
        idx = binary_search(subseq, number)
        print(f"{idx=}")
        # invariant: subseq is monotone increasing
        if subseq[-1] == number:
            print("flag1")
            continue
        if idx == 0 and subseq[0] > number:
            print("flag2")
            new_item = [1, [number]]
            if not tracker[1]:
                print("flag3")
                dp.append(new_item)
                continue
            else:
                print("flag4")
                new_subseq = new_item[1]
                indexed_item = choose(dp, 1)
                _, indexed_subseq = indexed_item
                smaller = indexed_subseq
                if comparator(indexed_subseq, new_subseq):
                    print("flag5")
                    smaller = new_subseq
                indexed_item[1] = smaller
                continue
        if not tracker[idx + 1]:
            print("flag6")
            tracker[idx] = True
            dp.append([idx, [*subseq[:idx - 1], number]])
            if idx > seen_max:
                tracker[seen_max] = False
                seen_max += 1
        else:
            print("flag7")
            # dp 에서 n이 idx인 원소를 찾아
            # 새로 생성한 subseq과 비교해 작은 것으로 update
            indexed_item = choose(dp, idx)
            _, indexed_subseq = indexed_item
            new_subseq = [*subseq[:idx-1], number]
            smaller = indexed_subseq
            if comparator(indexed_subseq, new_subseq):
                print("flag8")
                smaller = new_subseq
            indexed_item[1] = smaller
    return seen_max

def choose(dp, idx):
    # Q: is dp sorted?
    sorted_dp = sorted(dp, key=lambda item: item[0])
    left, right = 0, len(sorted_dp) - 1
    if sorted_dp[left][0] < idx:
        return None
    if sorted_dp[right][0] > idx:
        return None
    while True:
        mid = (left + right) // 2
        if left == mid:
            return sorted_dp[left]
        if sorted_dp[left][0] <= idx:
            left = mid
        else:
            right = mid

def comparator(arr1, arr2):
    assert len(arr1) == len(arr2)
    for num1, num2 in zip(arr1, arr2):
        if num1 > num2:
            return True
    return False

def longest_increasing_subsequence(numbers):
    n = len(numbers)
    assert n > 0, "invalid input"
    # tracker[idx] is True iff length of idx subsequence is tracked
    tracker = [False] * (n + 1)
    dp = [ [1, [numbers[0]] ] ]
    tracker[1] = True
    seen_max = 1

    for number in numbers:
        seen_max = update_dp(tracker, dp, number, seen_max)

    return seen_max

if __name__ == '__main__':
    numbers = [5, 3, 5, 10, 4, 1, 6, 8, 2]
    res = longest_increasing_subsequence(numbers)
    print(res)
