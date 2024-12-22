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
        # pprint(f'{array=}, {idx=}, {num=}')
        pprint(f'{idx=}, {num=}')
        if idx > maximum_index_of_non_leaf_node:
            return
        min_value = num
        is_target_left = None
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2 if n != idx * 2 + 2 else None

        # base condition: no need to swap
        if num > array[left_idx]:
            min_value = array[left_idx]
            is_target_left = True
        if right_idx and num > array[right_idx]:
            if is_target_left:
                if min_value > array[right_idx]:
                    min_value = array[right_idx]
                    is_target_left = False
            else:
                min_value = array[right_idx]
                is_target_left = False

        if is_target_left is not None:
            if is_target_left:
                array[idx], array[left_idx] = array[left_idx], array[idx]
                _heapify(left_idx, num)
            else:
                array[idx], array[right_idx] = array[right_idx], array[idx]
                _heapify(right_idx, num)

    pprint(f'=================')
    pprint(f'{array=}')
    n = len(array)
    if n <= 1:
        return array

    maximum_index_of_non_leaf_node = (n - 2) // 2
    non_leafs = array[:maximum_index_of_non_leaf_node + 1]
    # pprint(f'{maximum_index_of_non_leaf_node=}')
    # pprint(f'{array[:maximum_index_of_non_leaf_node + 1]=}')
    # pprint(f'{non_leafs=}')
    for idx, ele in reversed(list(enumerate(non_leafs))):
        _heapify(idx, ele)
    return array

if __name__ == '__main__':
    for i in range(11):
        array = sample(range(100), 20)
        heap = heapify(array)
        pprint(is_heap(heap))

