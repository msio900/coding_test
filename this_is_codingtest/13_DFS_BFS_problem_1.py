import sys
from collections import deque

f = sys.stdin.readline

N, M, K, X = map(int, f().split())
print(N, M, K, X)
graph = [[] for _ in range(N + 1)]
distance = [0] * (N+1)
visited = [False]*(N+1)

for _ in range(M):
    A, B = map(int, f().split())
    graph[A].append(B)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) ==0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(X)