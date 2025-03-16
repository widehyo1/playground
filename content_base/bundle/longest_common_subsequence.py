from typing import List
from enum import Enum, auto
from functools import reduce
from pprint import pprint, pformat

class Direction(Enum):
    DEFAULT = auto()
    UP = auto()
    LEFT = auto()
    UPLEFT = auto()
    UPANDLEFT = auto()

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.value == other.value

    def __repr__(self):
        name_info = {
            "DEFAULT": "-",
            "UP": "↑",
            "LEFT": "←",
            "UPLEFT": "↖",
            "UPANDLEFT": "⬑",
        }
        return name_info[self.name]

DEFAULT = Direction.DEFAULT
UP = Direction.UP
LEFT = Direction.LEFT
UPLEFT = Direction.UPLEFT
UPANDLEFT = Direction.UPANDLEFT

def longest_common_subsequence(x: str, y: str) -> str:
    def calc_element_value(row, col) -> tuple:
        """
        closure for calculate matrix with free variable:
        matrix
        """
        assert row > 0, f"invalid row index({row}) found"
        assert col > 0, f"invalid col index({col}) found"

        if tx[row] == ty[col]:
            value, dirction = matrix[row-1][col-1]
            matrix[row][col] = (value + 1, UPLEFT)
        else:
            left_element = matrix[row][col-1]
            l_value, _l_direction = left_element
            up_element = matrix[row-1][col]
            up_value, _up_direction = up_element
            if l_value > up_value:
                matrix[row][col] = (l_value, LEFT)
            elif l_value < up_value:
                matrix[row][col] = (up_value, UP)
            else:
                matrix[row][col] = (up_value, UPANDLEFT)
        return matrix[row][col]

    if len(x) == 0 or len(y) == 0:
        return ""

    tx = f" {x}"
    ty = f" {y}"
    row_cnt = len(tx)
    col_cnt = len(ty)

    matrix = [[(0, DEFAULT)] * col_cnt for _ in range(row_cnt)]
    for ix in range(1, row_cnt):
        for iy in range(1, col_cnt):
            calc_element_value(ix, iy)
    visualized_matrix(tx, ty, matrix)

    cur_row = row_cnt - 1
    cur_col = col_cnt - 1

    result = ""
    while cur_row > 0 and cur_col > 0:
        cur_item = matrix[cur_row][cur_col]
        cur_value, cur_direction = cur_item
        if cur_direction in set([UP, UPANDLEFT]):
            cur_row -= 1
        elif cur_direction is LEFT:
            cur_col -= 1
        elif cur_direction is UPLEFT:
            result = tx[cur_row] + result # or result = ty[cur_col] + result
            cur_row -= 1
            cur_col -= 1
        elif cur_direction is DEFAULT:
            print("error")
            break
    return result

def visualized_matrix(tx: str, ty: str, matrix: List):
    print(f"•|" + "     |".join(ty))
    for idx, _ in enumerate(matrix):
        row_repr = reduce(reducer, matrix[idx], tx[idx])
        print(row_repr)

def reducer(acc, cur) -> str:
    return f"{acc}|{cur}"


if __name__ == "__main__":
#     x = "XMJYAUZ"
#     x = "XMJY"
    x = "QYGP"
    y = "MZJAWXU"
    lcs = longest_common_subsequence(x, y)
    print(lcs)
