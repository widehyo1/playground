inputs = [5,9,16,12,8,11,13,8,7,3]

def merge(arr1, arr2):
    p1 = p2 = 0
    n1 = len(arr1)
    n2 = len(arr2)
    print(f"{arr1=}, {arr2=}")
    def gen():
        nonlocal p1, p2, n1, n2
        while p1 < n1 and p2 < n2:
            print(f"{p1=}, {p2=}")
            if arr1[p1] <= arr2[p2]:
                yield arr1[p1]
                p1 += 1
            else:
                yield arr2[p2]
                p2 += 1
        if p1 < n1:
            print("flag1")
            print(f"{arr1[p1:]}")
            yield from arr1[p1:]
        if p2 < n2:
            print("flag2")
            print(f"{arr2[p2:]}")
            yield from arr2[p2:]
    return list(gen())


def merge_sort(lis):
    if len(lis) <= 1: return lis
    mid = len(lis) // 2
    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])

    return merge(left, right)

def main():
    print(inputs)
    ret = merge_sort(inputs)
    print(ret)


if __name__ == '__main__':
    main()

