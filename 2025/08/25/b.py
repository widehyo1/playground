# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 
# (0,0),(0,1),(0,2),
# (1,0),(1,1),(1,2),
# (2,0),(2,1),(2,2)
# 
# 순서:
# step1: (0,0)
# step2: (0,1),(1,0) [(2, -1) >> (2,0)]
# step3: (2,0),(1,1),(0,2) [(-1, 3) >> (0, 3) >> (1, 2)] UR 
# step4: (1,2),(2,1)
# step5: (2,2)
# 
# (0,0,row)
# (0,1,col)
# (1,0,row)
# 
# 벽에 닿을 때 까지
# 0에 도달하거나, 
# 가로시작
# 
# 가로합 + 세로합이 1씩 증가
# 
# [[1,2,3,4]]?
# 1>2>3>4
# [[1],[2],[3],[4]]
# 1>2>3>4
# 
# flatten이긴 하네
# 
# [[1,2,3],
#  [4,5,6]]
# step1: (0,0)
# step2: (0,1),(1,0)
# step3: (1,1),(0,2)
# step4: (1,2)
# 
# 2 * 3 matrix
# step, dir = 0, ur
# step, dir = 1, dl (1,0)까지 가고 (2,-1)이 되니 방향 반전 현상태: (1,0) toggle (2,0)가능? 불가능 그럼 다음것 올림
# step, dir = 2, ur 왜 (2,0)이 아니라 (1,1)인가? 그리고 이때 무슨 일이 일어나나?
# step, dir = 3, dl
# step, dir = 4, ur
# 
# step과 direction으로 구분
# step은 가로 + 세로 인덱스의 합
# direction은 우상향 시작, 좌하향 반전
# 우상향, 좌하향 토글
# 
# 토글 조건?
# 
# 
# turn의 개념?
# start, 세로 turn, 가로 turn
# 각 turn에 맞는 index가 증가

def findDiagonalOrder(self, mat: list[list[int]]) -> List[int]:
    step = 0
    direction = "UR"
    m = len(mat)
    n = len(mat[0])

    row = col = 0

    res = []

    while step < m + n:
        res.append(mat[row][col])


# (0,0),(0,1),(0,2),
# (1,0),(1,1),(1,2),
# (2,0),(2,1),(2,2)
# 
# 순서:
# step1: (0,0)
# step2: (0,1),(1,0) [(2, -1) >> (2,0)]
# step3: (2,0),(1,1),(0,2) [1. 우상향이 있다면 그 값을 쓴다. 2. 상단이 없고 우측이 있다면 우측을 쓴다(그리고 방향을 바꾼다). 3. 우측도 없다면 아래로 이동후 좌하향 방향으로 바꾼다]

# [[1,2,3,4]]?
# 1>2>3>4
# [[1],
# [2],
# [3],
# [4]]
# (0,0) > (-1, 1) (0, 1), (1, 0)
# (1,0) > (2, -1) >> (2, 0)
# (2,0) > *[(1, 1) ] (,1)이 없다! [1. 우상향 없음, 2. 상단있으나 우측 없음.  같은 방법으로 처리 가능
# 1>2>3>4
# 
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
            
# [[1,2,3],
#  [4,5,6]]
# step1: (0,0)
# step2: (0,1),(1,0)
# step3: (1,1),(0,2)
# step4: (1,2)
# 
# 2 * 3 matrix

# step2: (0,1),(1,0) [1. 좌하향이 있으면 그 값을 쓴다. 2. 좌가 없으면 아래가 있을 때 아래를 쓴다.(그리고 방향을 바꾼다) 3. 아래도 없다면 우측으로 바꾸고 우상향 방향을 본다]
# step3: (1,1),(0,2) (
    return res

