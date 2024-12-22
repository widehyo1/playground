from typing import List
from pprint import pprint
from random import sample

def is_heap(heap: List[int]) -> bool:
    n = len(heap)
    for idx, element in reversed(list(enumerate(heap[1:], 1))):
        # walks on non-root nodes
        parent_idx = (idx - 1) // 2
        if element < heap[parent_idx]:
            return False
    return True


def heapify(array: List[int]) -> List[int]:
    """
    make minimum heap
    the index of non-leaf node
    |len|maximum_index_of_non_leaf_node|
    |---|---|
    |1|None|
    |2|0|
    |3|0|
    |4|1|
    |5|1|
    |6|2|
    |7|2|
    """
    def _heapify(idx: int, num: int):
        """
        closure for inplace array
        free variable is: array, n
        """
        min_idx = idx
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2

        if left_idx < n and array[left_idx] < array[min_idx]:
            min_idx = left_idx
        if right_idx < n and array[right_idx] < array[min_idx]:
            min_idx = right_idx

        if min_idx != idx:
            array[idx], array[min_idx] = array[min_idx], array[idx]
            _heapify(min_idx, num)

    n = len(array)
    if n <= 1:
        return array

    maximum_index_of_non_leaf_node = (n - 2) // 2
    non_leafs = array[:maximum_index_of_non_leaf_node + 1]
    for idx, ele in reversed(list(enumerate(non_leafs))):
        _heapify(idx, ele)
    return array

if __name__ == '__main__':
    for i in range(11):
        array = sample(range(100), 20)
        heap = heapify(array)
        pprint(heap)
        pprint(is_heap(heap))

