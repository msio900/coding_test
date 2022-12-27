import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
min_d = [INF] * (V+1)
graph = [[] for _ in range(V + 1)]
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

min_d[K] = 0
heapq.heappush(heap, (0, K))

while heap:
    distance, node = heapq.heappop(heap)

    if min_d[node] < distance:
        continue
    for dis, nxt_node in graph[node]:
        nxt_dis = dis + distance
        if nxt_dis < min_d[nxt_node]:
            min_d[nxt_node] = nxt_dis
            heapq.heappush(heap, (nxt_dis, nxt_node))


for i in range(1, V+1):
    print("INF" if min_d[i] == INF else min_d[i])