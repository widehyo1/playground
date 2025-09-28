from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    n = len(points)

    if k > n:
        raise ValueError("invalid input")
    if k == n:
        return points

    distances = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
    heapq.heapify(distances)
    result = []
    for _ in range(k):
        item = heapq.heappop(distances)
        distance, point = item
        result.append(point)
    return result

points = [[2,2], [1,3]]
kClosest(points, 1)



def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    n = len(points)

    if k > n:
        raise ValueError("invalid input")
    if k == n:
        return points

    distances = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
    heapq.heapify(distances)
    result = []
    for _ in range(k):
        item = heapq.heappop(distances)
        distance, point = item
        result.append(point)
    return result
