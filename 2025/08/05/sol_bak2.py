from bisect import bisect_left

def predicate_factory(arr, num):
    def predicate(idx):
        print(f"{arr=}, {idx=}, {num=}")
        return arr[idx] <= num

    return predicate


def binary_search_ridx(arr, num):
    """
    find the first index k such that
    predicate(0) is True
    predicate(1) is True
    ...
    predicate(k-1) is True
    predicate(k) is False
    ...
    predicate(n-2) is False
    predicate(n-1) is False

    with edge cases:
    predicate(0) is False -> return 0
    predicate(n-1) is True -> return n
    """
    n = len(arr)
    if n == 0:
        return 0
    predicate = predicate_factory(arr, num)
    left = 0
    if not predicate(left):
        return 0
    right = n - 1
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


class IncreasingSequence:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, idx, value):
        self.data[idx] = value

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for e1, e2 in zip(self.data, other.data):
            if e1 != e2:
                return False
        return True

    def __gt__(self, other):
        if type(self) != type(other):
            raise RuntimeError("invalid type comparison")
        return self.data > other.data

    def min_(self):
        assert len(self)
        return self[0]

    def max_(self):
        assert len(self)
        return self[-1]

    def update(self, number):
        print(f"update with number: {number}")
        ridx = binary_search_ridx(self.data, number)
        if ridx == 0:
            print("new sequence")
            print(bisect_left(self.data, number), ridx)
        elif ridx == len(self):
            print("inc_seq lengthen")
            self.data.append(number)
            print(bisect_left(self.data, number), ridx)
        else:
            if self[ridx - 1] == number:
                print("pass")
                print(bisect_left(self.data, number), ridx - 1)
                return ridx - 1
            else:
                print("update")
                print(bisect_left(self.data, number), ridx)
                self[ridx] = number
        return ridx

    def __repr__(self):
        return f"<IncreasingSequence {self.data} >"


def get_longest_increasing_sequence(numbers):
    n = len(numbers)
    if n == 0:
        return numbers

    tracker = dict()
    head = numbers[0]
    seen_max = head
    result = 1

    head_seq = IncreasingSequence([head])
    tracker[1] = head_seq

    for i in range(1, n):
        print(tracker)
        number = numbers[i]

        for key, inc_seq in reversed(sorted(tracker.items())):
            position = inc_seq.update(number)
            if position == key:
                # lengthen inc_seq
                tracker[key + 1] = min(tracker.get(key + 1, inc_seq), inc_seq)
                result = max(result, key + 1)
                del tracker[key]
            if position == 0:
                new_seq = IncreasingSequence([number])
                tracker[1] = min(tracker.get(1, new_seq), new_seq)

    print(tracker)
    return result


if __name__ == "__main__":
    numbers = [14, 17, 15, 4, 18, 13, 8, 1, 15, 14, 16]
    result = get_longest_increasing_sequence(numbers)
    print(result)
