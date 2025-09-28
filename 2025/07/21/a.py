# def arrangeCoins(n):
#     # 1, 3, 6, 10, 15, ..
#     # sum of n: n(n+1) / 2
#     result = 1
#     while result * (result + 1) / 2 <= n:
#         result += 1
#     return result - 1

def arrangeCoins(n):
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        print(f"{left=}, {right=}, {mid=}")
        print(f"{(mid * (mid + 1) / 2)=}, {n=}")
        if mid * (mid + 1) / 2 < n:
            left = mid + 1
        elif mid * (mid + 1) == n:
            return mid - 1
        else:
            right = mid - 1
    return left

if __name__ == '__main__':
    nums = [1, 5, 8]
    # for num in nums:
    for num in range(1, 11):
        print(f"{num=}")
        print(arrangeCoins(num))
