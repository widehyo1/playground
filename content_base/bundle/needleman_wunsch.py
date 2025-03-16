from typing import List
from enum import Flag, auto
from functools import reduce
from pprint import pprint, pformat


class Direction(Flag):
    DEFAULT = auto()
    UP = auto()
    LEFT = auto()
    UPLEFT = auto()

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
        }

        # If it's a single flag, return the mapped symbol
        if self._value_ in name_info:
            return name_info[self.name]
        # Otherwise, return a combination of flags
        active_flags = [name_info[flag.name] for flag in Direction if (self & flag)]
        return "|".join(active_flags)


DEFAULT = Direction.DEFAULT
UP = Direction.UP
LEFT = Direction.LEFT
UPLEFT = Direction.UPLEFT


def needleman_wunsch(x: str, y: str) -> str:
    def calc_element_value(
        row: int,
        col: int,
        /,
        match_value: int = 1,
        mis_match_value: int = -1,
        gap_penalty: int = -1,
    ) -> tuple:
        """
        closure for calculate matrix with free variable:
        matrix, tx, ty
        """
        assert row > 0, f"invalid row index({row}) found"
        assert col > 0, f"invalid col index({col}) found"

        diag_element = matrix[row - 1][col - 1]
        left_element = matrix[row][col - 1]
        up_element = matrix[row - 1][col]

        diag_value, _diag_direction = diag_element
        l_value, _l_direction = left_element
        up_value, _up_direction = up_element

        s_value = mis_match_value
        if tx[row] == ty[col]:
            s_value = match_value

        candidate_l = l_value + gap_penalty
        candidate_up = up_value + gap_penalty
        candidate_diag = diag_value + s_value

        element_value = max(candidate_l, candidate_up, candidate_diag)
        element_direction = DEFAULT

        base_direction = UP | LEFT | UPLEFT

        if element_value == candidate_l:
            element_direction |= LEFT
        if element_value == candidate_up:
            element_direction |= UP
        if element_value == candidate_diag:
            element_direction |= UPLEFT

        element_direction = element_direction & base_direction

        matrix[row][col] = (element_value, element_direction)

        return matrix[row][col]

    if len(x) == 0 or len(y) == 0:
        return ""

    tx = f" {x}"
    ty = f" {y}"
    row_cnt = len(tx)
    col_cnt = len(ty)

    matrix = [[(0, DEFAULT)] * col_cnt for _ in range(row_cnt)]
    # initialize first row
    for idx, _ in enumerate(matrix[0]):
        matrix[0][idx] = (-idx, DEFAULT)
    # initialize first column
    for idx, _ in enumerate(matrix):
        matrix[idx][0] = (-idx, DEFAULT)

    for ix in range(1, row_cnt):
        for iy in range(1, col_cnt):
            calc_element_value(ix, iy)
    visualized_matrix(tx, ty, matrix)

    cur_row = row_cnt - 1
    cur_col = col_cnt - 1

    result = ""
    while cur_row > 0 and cur_col > 0:
        cur_item = matrix[cur_row][cur_col]
        #         print(f"cur_item: {repr(cur_item)}, cur_row: {cur_row}, cur_col: {cur_col}")
        #         print(f"result: {result}")
        cur_value, cur_direction = cur_item
        if UP & cur_direction:
            cur_row -= 1
            result = "-" + result
        elif LEFT & cur_direction:
            cur_col -= 1
            result = "-" + result
        elif UPLEFT & cur_direction:
            result = tx[cur_row] + result  # or result = result + ty[cur_col]
            cur_row -= 1
            cur_col -= 1
        elif cur_direction is DEFAULT:
            print("error")
            break
    return result


def visualized_matrix(tx: str, ty: str, matrix: List):
    print(f"•|" + "          |".join(ty))
    for idx, _ in enumerate(matrix):
        row_repr = reduce(reducer, matrix[idx], tx[idx])
        print(row_repr)


def reducer(acc, cur) -> str:
    value, direction = cur
    return f"{acc}|({value:+03},{repr(direction):>5})"


if __name__ == "__main__":
    x = "XMJYAUZ"
    y = "MZJAWXU"
    result = needleman_wunsch(x, y)
    print(result)
