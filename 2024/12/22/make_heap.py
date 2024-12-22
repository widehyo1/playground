from typing import List
from random import sample

def is_heap(heap: List[int]) -> bool:
    n = len(heap)
    for idx, element in reversed(list(enumerate(heap[1:], 1))):
        # walks on non-root nodes
        parent_idx = (idx - 1) // 2
        if element < heap[parent_idx]:
            return False
    return True

def add_to_head(heap: List[int], target: int):
    n = len(heap)
    if n == 0:
        heap.append(target)
        return heap
    heap.append(target)
    target_idx = n
    while target_idx != 0:
        # target index is updated iff swap occurs
        # 1. find parent_idx
        # 2. determine swap or not
        # 3. if swap, update target_idx
        parent_idx = (target_idx - 1) // 2
        if target <= heap[parent_idx]:
            # swap condition
            heap[target_idx], heap[parent_idx] = heap[parent_idx], heap[target_idx]
            target_idx = parent_idx
        else:
            break
    return heap

def make_heap(array: List[int]) -> List[int]:
    """
    make minimun heap
    """
    heap = []
    for ele in array:
        add_to_head(heap, ele)
    return heap

if __name__ == '__main__':
    array = sample(range(10), 6)
    heap = make_heap(array)

