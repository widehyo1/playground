from functools import wraps

bk = breakpoint

def print_result(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print(f'=== {func.__name__} start ===')
        result = func(*args, **kwargs)
        print(f'result: {result}')
        print(f'=== {func.__name__} end ===')
        return result
    return decorator

class DisjointSet:
    def __init__(self, name, parent=None, rank=0):
        self.name = name
        self.parent = parent if parent else self
        self.rank = 0

    def __repr__(self):
        if self.parent is not self:
            return f'<DisjointSet {self.name}({self.rank}) -> {self.parent}>'
        else:
            return f'<DisjointSet {self.name}({self.rank})*>'

@print_result
def make_set(name) -> DisjointSet:
    return DisjointSet(name)

@print_result
def find(ds: DisjointSet) -> DisjointSet:
    # base condition
    if ds.parent is ds:
        return ds
    # biz logic
    return find(ds.parent)

@print_result
def find_advanced(ds: DisjointSet) -> DisjointSet:
    # base condition
    if ds.parent is ds:
        return ds
    # biz logic
    ds.parent = find(ds.parent)
    return ds.parent

def union(fst: DisjointSet, snd: DisjointSet) -> None:
    fst.parent = snd

def union_advanced(fst: DisjointSet, snd: DisjointSet) -> None:
    # get_root = find
    get_root = find_advanced
    fst_root = get_root(fst)
    snd_root = get_root(snd)

    # base condition
    if fst_root is snd_root:
        return

    if fst_root.rank > snd_root.rank:
        snd_root.parent = fst_root
    elif fst_root.rank < snd_root.rank:
        fst_root.parent = snd_root
    else:
        fst_root.parent = snd_root
        snd_root.rank = snd_root.rank + 1

def main():

    a = make_set(1)
    b = make_set(2)
    c = make_set(3)
    d = make_set(4)
    e = make_set(5)

    print(a)
    print(b)

    union_advanced(a, b)
    union_advanced(d, e)
    union_advanced(c, a)
    union_advanced(c, b)
    union_advanced(b, d)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == '__main__':
    main()
