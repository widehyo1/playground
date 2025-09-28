from typing import List
import heapq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    n = len(points)
    print("flag1")

    if k > n:
        raise ValueError("invalid input")
    if k == n:
        return points

    print("flag2")
    print("asdf")
    distances = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
    heapq.heapify(distances)
    print(distances)
    result = []
    for _ in range(k):
        item = heapq.heappop(distances)
        distance, point = item
        result.append(point)
    print(result)
    return result

print("qwer")
points = [[2,2], [1,3]]
kClosest(points, 1)


