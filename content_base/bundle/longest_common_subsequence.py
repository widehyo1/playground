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

        if self._value_ in name_info:
            return name_info[self.name]
        active_flags = [name_info[flag.name] for flag in Direction if (self & flag)]
        return "|".join(active_flags)


DEFAULT = Direction.DEFAULT
UP = Direction.UP
LEFT = Direction.LEFT
UPLEFT = Direction.UPLEFT


def longest_common_subsequence(x: str, y: str) -> str:
    def calc_element_value(row, col) -> tuple:
        """
        closure for calculate matrix with free variable:
        matrix
        """
        assert row > 0, f"invalid row index({row}) found"
        assert col > 0, f"invalid col index({col}) found"

        if tx[row] == ty[col]:
            value, dirction = matrix[row - 1][col - 1]
            matrix[row][col] = (value + 1, UPLEFT)
        else:
            left_element = matrix[row][col - 1]
            l_value, _l_direction = left_element
            up_element = matrix[row - 1][col]
            up_value, _up_direction = up_element

            base_direction = UP | LEFT

            element_value = max(l_value, up_value)
            element_direction = DEFAULT

            if l_value == element_value:
                element_direction |= LEFT
            if up_value == element_value:
                element_direction |= UP
            # restrict direction to LEFT and UP
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
    for ix in range(1, row_cnt):
        for iy in range(1, col_cnt):
            calc_element_value(ix, iy)
    visualized_matrix(tx, ty, matrix)

    cur_row = row_cnt - 1
    cur_col = col_cnt - 1
    x_result = ""  # x based result
    y_result = ""  # y based result

    stack = [(cur_row, cur_col, x_result, y_result)]
    result_list = []
    result_set = set()

    while stack:
        cur_row, cur_col, x_result, y_result = stack.pop()
        # base condition
        if cur_col == 0:
            x_result = cur_row * "-" + x_result
            if (x_result, y_result) not in result_set:
                result_set.add((x_result, y_result))
                result_list.append((x_result, y_result))
            if len(stack) > 1:
                stack.pop()
            continue
        if cur_row == 0:
            y_result = cur_col * "-" + y_result
            if (x_result, y_result) not in result_set:
                result_set.add((x_result, y_result))
                result_list.append((x_result, y_result))
            if len(stack) > 1:
                stack.pop()
            continue
        cur_item = matrix[cur_row][cur_col]
        cur_value, cur_direction = cur_item
        if cur_direction & LEFT:
            stack.append((cur_row, cur_col - 1, x_result, "-" + y_result))
        if cur_direction & UP:
            stack.append((cur_row - 1, cur_col, "-" + x_result, y_result))
        if cur_direction & UPLEFT:
            stack.append(
                (
                    cur_row - 1,
                    cur_col - 1,
                    tx[cur_row] + x_result,
                    ty[cur_col] + y_result,
                )
            )
        elif cur_direction is DEFAULT:
            print("error")
            break

    return result_list


def visualized_matrix(tx: str, ty: str, matrix: List):
    print(f"•|" + "          |".join(ty))
    for idx, _ in enumerate(matrix):
        row_repr = reduce(reducer, matrix[idx], tx[idx])
        print(row_repr)


def reducer(acc, cur) -> str:
    value, direction = cur
    return f"{acc}|({value:+03},{repr(direction):>5})"


if __name__ == "__main__":
    #     x = "XMJYAUZ"
    #     x = "XMJY"
    #     y = "MZJAWXU"
    #     x = "GAC"
    #     y = "AGCAT"
    #     x = "Reading out a LCS"
    #     y = "Reading out all LCSs"
    #     x = "Reading out all LCSs"
    #     y = "Reading out a LCS"
    x = "XMJYAUZ"
    y = "MZJAWXU"
    lcs = longest_common_subsequence(x, y)
    print(lcs)
