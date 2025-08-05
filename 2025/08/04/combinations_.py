def combinations(arr):
    n = len(arr)

    def backtrack(idx, comb):
        if idx == n:
            print(comb)
            return
        item = arr[idx]
        comb.append(item)
        backtrack(idx + 1, comb)
        comb.pop()
        backtrack(idx + 1, comb)

    backtrack(0, [])

if __name__ == '__main__':
    arr = [1, 2, 3]
    combinations(arr)
