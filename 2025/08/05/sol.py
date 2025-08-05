def predicate_factory(arr, num):
    def predicate(idx):
        return arr[idx] <= num

    return predicate


def binary_search_ridx(arr, num):
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
        ridx = binary_search_ridx(self.data, number)

        if ridx == 0:
            return 0
        if self[ridx - 1] == number:
            return ridx - 1
        if ridx == len(self):
            self.data.append(number)
        else:
            self[ridx] = number
        return ridx

    def __repr__(self):
        return f"<IncreasingSequence {self.data} >"


def get_longest_increasing_sequence(numbers):
    if len(numbers) == 0:
        return 0
    head = numbers[0]
    tails = IncreasingSequence([head])
    for number in numbers[1:]:
        print(tails)
        position = tails.update(number)
        if position == 0:
            tails[0] = number
    print(tails)
    return len(tails)


if __name__ == "__main__":
    numbers = [14, 17, 15, 4, 18, 13, 8, 1, 15, 14, 16]
    result = get_longest_increasing_sequence(numbers)
    print(result)
