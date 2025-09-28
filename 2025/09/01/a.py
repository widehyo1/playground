from pprint import pp
from collections import defaultdict
import heapq
V, E = [int(_) for _ in input().split()]
start_node = int(input())

adjacent_array = defaultdict(list)

# 여기서 넣을 때 최소거리만 남겨야겠다.
# 인접행렬 대신 tuple(start, end) 를 키로, weight를 value로 가지는 dict로 모델링해야할듯
for _ in range(E):
    edge = [int(_) for _ in input().split()]
    start, end, weight = edge
    adjacent_array[start].append((weight, end))

print(V, E)
print(start_node)
print(adjacent_array)

def gen_edge_info(adjacent_array):
    for key, edges in adjacent_array.items():
        for edge in edges:
            yield edge, key

heap = list((edge, key) for edge, key in gen_edge_info(adjacent_array))
heapq.heapify(heap)
print(heap)
#     print(key, edge)
#     wieght, end = edge
#     print(weight, end)

# construct matrix
# init matrix
# 이거 플로이드 워셜인가 벨만포드인가 같은데
# 다익스트라는 1차원 배열아니었나
# distances = [[1e7 for _ in range(V)] for _ in range(V)]
# for i in range(V):
#     distances[i][i] = 0
# 
# while heap:
#     pp(distances)
#     cur = heapq.heappop(heap)
#     print(cur)
#     edge, start = cur
#     weight, end = edge
#     print(start, end, weight)
#     # 갱신
#     for t in range(V):
#         if distances[start-1][t] + distances[t][end-1] > weight:
#     if distances[start-1][end-1] + weight < 
#     distances[start-1][end-1] = distances[end-1][start-1] = min(distances[start-1][end-1], weight)
#     
# pp(distances)

distances = [1e7 for _ in range(V)]
distances[start_node-1] = 0

# while heap:
#     pp(distances)
#     cur = heapq.heappop(heap)
#     print(cur)
#     edge, start = cur
#     weight, end = edge
#     print(start, end, weight)
# 
#     for t in range(V):
#         if distances[start_node-1] + distances[t]

visited = [False] * V

cur = start_node - 1
for edge in adjacent_array[start_node-1]:
    weight, end = edge
    # visited[

# 다익스트라 어캐풀더라

# print(distances)
# print(len(distances))
# print(len(distances[0]))
# 3개
#   1 2 3
# 1 0 e
# 2   0
# 3     0
#
# 시작점 중심으로 뻗어나간다?
# 기억이 안남

