from operator import itemgetter
from itertools import (
    zip_longest as zl,
    groupby,
)

SENTINEL = object()

def gen_roundrobin(*iterables):
    return (item for tup in zl(*iterables, fillvalue=SENTINEL)
                 for item in tup if item is not SENTINEL)

def gen_transpose(*iterables):
    it_roundrobin_with_index = (
        (idx, item)
        for idx, tup in enumerate(zl(*iterables, fillvalue=SENTINEL))
        for item in tup if item is not SENTINEL
    )
    for _colidx, it_col in groupby(it_roundrobin_with_index, itemgetter(0)):
        yield (item for _, item in it_col)

a = [1, 2, 3]
b = [4, 5]
c = [6, 7, 8, 9]
print(list(gen_roundrobin(a, b, c)))
for it_col in gen_transpose(a, b, c):
    print(it_col)
    print(list(it_col))
