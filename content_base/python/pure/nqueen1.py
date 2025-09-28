def sol(n: int) -> list[tuple] | None:
    if n <= 3: return None

    rowset = set()
    colset = set()

    results = []
    candidate = []

    # free variables: n, rowset, colset, candidate
    def gen_rowfilter():
        for i in range(n):
            if i not in rowset:
                yield i

    def gen_colfilter():
        for j in range(n):
            if j not in colset:
                yield j

    def check_diag(i: int, j: int):
        for item in candidate:
            k, l = item
            if abs(k - i) == abs(l - j):
                return True
        return False

    def put(row: int, col: int):
        rowset.add(row)
        colset.add(col)
        candidate.append((row, col))

    def reset():
        rowset.clear()
        colset.clear()
        candidate.clear()

    def find_positions(row):
        put(row, 0)
        print(f"{row=}")
        print(f"{rowset=}")
        print(f"{colset=}")
        print(f"{candidate=}")
        for x in gen_rowfilter():
            for y in gen_colfilter():
                if not check_diag(x, y):
                    put(x, y)
                    print(f"{x=}, {y=}")
                    print(f"{rowset=}")
                    print(f"{colset=}")
                    print(f"{candidate=}")
                    if len(candidate) == n:
                        print("if")
                        results.append(list(candidate))
                        print(f"{results=}")
                    else:
                        print("else")

    for row in range(n):
        reset()
        find_positions(row)

    print(f"{results=}")
    print(f"{len(results)=}")

if __name__ == '__main__':
    sol(4)

