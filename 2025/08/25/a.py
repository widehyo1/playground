def findDiagonalOrder(self, mat: list[list[int]]) -> List[int]:
    step = 0
    direction = "UR"
    m = len(mat)
    n = len(mat[0])

    row = col = 0

    res = []

    while step < m + n:
        res.append(mat[row][col])
        if direction == "UR":
            nxt_row = row - 1
            nxt_col = col + 1

            # 위의 값이 없다면
            if nxt_row < 0:
                # 우측이 없다면
                if nxt_col >= n:
                    # 아래로 이동
                    row = row + 1
                else:
                    # 우측이 있다면 우측으로 update
                    col = nxt_col
            else:
                row = nxt_row
                col = nxt_col

            # step, direction 결정
            if row < 0 or col >= n:
                direction = "DL"
                step = step + 1

        elif direction == "DL":
            nxt_row = row + 1
            nxt_col = col - 1
            # 좌측 값이 없다면
            if nxt_col < 0:
                # 하향이 없다면
                if nxt_row >= m:
                    # 우측으로 이동
                    col = col + 1
                else:
                    # 하향이 있다면 하향으로 이동
                    row = nxt_row
            else:
                row = nxt_row
                col = nxt_col

            if col < 0 or row >= m:
                direction = "UR"
                step = step + 1
    return res

