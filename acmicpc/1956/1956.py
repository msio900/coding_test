import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[]for _ in range(v+1)]

dist = [[1e9] * (v+1) for _ in range(v+1)]

heap = []
for _ in range(e):
    x, y, c = map(int, input().split())
    graph[x].append([c, y])
    dist[x][y] = c
    heapq.heappush(heap, [c, x, y])


while heap:

    d, s, g = heapq.heappop(heap)


    if s == g:
        print(d)
        break
    if dist[s][g] < d:
        continue

    for nd, ng in graph[g]:

        new_d = d + nd

        if new_d < dist[s][ng]:
            dist[s][ng] = new_d
            heapq.heappush(heap, [new_d, s, ng])

else:
    print(-1)


