from typing import List
from functools import reduce
from pprint import pprint, pformat


class Direction:
    def __init__(self, val: int = 0b000):
        """
        self.val is a representation of direction
        up:      0b001
        left:    0b010
        upleft:  0b100
        default: 0b000

        each direction acts as a flag, thus it can be overrapped
        """
        self.val = val

    def __repr__(self):
        rep_list = []
        if self.val & 0b001:  # test it contains up direction
            rep_list.append("↑")
        if self.val & 0b010:  # test it contains left direction
            rep_list.append("←")
        if self.val & 0b100:  # test it contains upleft direction
            rep_list.append("↖")

        if len(rep_list) == 0:
            return "-"
        return "|".join(rep_list)


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
        element_direction = Direction()

        if element_value == candidate_up:
            element_direction.val |= 0b001
        if element_value == candidate_l:
            element_direction.val |= 0b010
        if element_value == candidate_diag:
            element_direction.val |= 0b100

        matrix[row][col] = (element_value, element_direction)

        return matrix[row][col]

    if len(x) == 0 or len(y) == 0:
        return ""

    tx = f" {x}"
    ty = f" {y}"
    row_cnt = len(tx)
    col_cnt = len(ty)

    matrix = [[(0, Direction())] * col_cnt for _ in range(row_cnt)]
    # initialize first row
    for idx, _ in enumerate(matrix[0]):
        matrix[0][idx] = (-idx, Direction())
    # initialize first column
    for idx, _ in enumerate(matrix):
        matrix[idx][0] = (-idx, Direction())

    for ix in range(1, row_cnt):
        for iy in range(1, col_cnt):
            calc_element_value(ix, iy)
    visualized_matrix(tx, ty, matrix)

    cur_row = row_cnt - 1
    cur_col = col_cnt - 1
    x_result = ""
    y_result = ""

    stack = [(cur_row, cur_col, x_result, y_result)]

    result_list = []
    result_set = set()

    while stack:
        cur_row, cur_col, x_result, y_result = stack.pop()
        # base condition
        if cur_row == 0:
            y_result = cur_col * "-" + y_result
            if (x_result, y_result) not in result_set:
                result_set.add((x_result, y_result))
                result_list.append((x_result, y_result))
            if len(stack) > 1:
                stack.pop()
            continue
        if cur_col == 0:
            x_result = cur_row * "-" + x_result
            if (x_result, y_result) not in result_set:
                result_set.add((x_result, y_result))
                result_list.append((x_result, y_result))
            if len(stack) > 1:
                stack.pop()
            continue

        cur_item = matrix[cur_row][cur_col]
        cur_value, cur_direction = cur_item

        if cur_direction.val & 0b001:
            stack.append((cur_row - 1, cur_col, "-" + x_result, y_result))
        if cur_direction.val & 0b010:
            stack.append((cur_row, cur_col - 1, x_result, "-" + y_result))
        if cur_direction.val & 0b100:
            stack.append(
                (
                    cur_row - 1,
                    cur_col - 1,
                    tx[cur_row] + x_result,
                    ty[cur_col] + y_result,
                )
            )
        if cur_direction.val == 0b000:
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
    x = "XMJYAUZ"
    y = "MZJAWXU"
    result = needleman_wunsch(x, y)
    print(result)
