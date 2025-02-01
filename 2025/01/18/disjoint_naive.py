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
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent if parent else self

    def __repr__(self):
        if self.parent is not self:
            return f'<DisjointSet {self.name} -> {self.parent}>'
        else:
            return f'<DisjointSet {self.name}*>'

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

def union(fst: DisjointSet, snd: DisjointSet) -> None:
    fst.parent = snd

def main():
    get_root = find

    a = make_set(1)
    b = make_set(2)
    c = make_set(3)
    d = make_set(4)
    e = make_set(5)

    print(a)
    print(b)

    union(a, b)
    union(d, e)
    union(c, a)
    union(c, b)
    union(b, d)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    get_root(a)
    get_root(b)
    get_root(c)
    get_root(d)
    get_root(e)


if __name__ == '__main__':
    main()
