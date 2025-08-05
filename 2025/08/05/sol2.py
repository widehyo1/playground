from bisect import bisect_left

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
        if bisect_left(self.data, number) == len(self):
            self.data.append(number)
        else:
            self.data[bisect_left(self.data, number)] = number

    def __repr__(self):
        return f"<IncreasingSequence {self.data} >"


def get_longest_increasing_sequence(numbers):
    if len(numbers) == 0:
        return 0
    head = numbers[0]
    tails = IncreasingSequence([head])
    for number in numbers[1:]:
        tails.update(number)
    return len(tails)


if __name__ == "__main__":
    numbers = [14, 17, 15, 4, 18, 13, 8, 1, 15, 14, 16]
    result = get_longest_increasing_sequence(numbers)
    print(result)
