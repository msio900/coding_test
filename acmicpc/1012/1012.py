# from collections import deque
#
# case = int(input())
#
# mx = [0, 0, 1, -1]
# my = [1, -1, 0, 0]
# def bfs(x, y):
#     queue = deque()
#     queue.append([x,y])
#     visited[x][y] = 1
#     while queue:
#         nx, ny = queue.popleft()
#         for i in range(4):
#             dx = mx[i] + nx
#             dy = my[i] + ny
#
#             if 0 <= dx < M and 0 <= dy < N and visited[dx][dy] == 0 and graph[dx][dy] ==1:
#                 queue.append([dx, dy])
#                 visited[dx][dy] = 1
#
# for c in range(case):
#     M, N, K = map(int, input().split())
#
#     graph = [[0 for i in range(N)] for j in range(M)]
#     visited = [[0 for i in range(N)] for j in range(M)]
#
#     for k in range(K):
#         a, b = map(int, input().split())
#         graph[a][b] = 1
#         answer = 0
#         for i in range(M):
#             for j in range(N):
#                 if graph[i][j] == 1 and visited[i][j] ==0:
#                     bfs(i, j)
#                     answer += 1
#
#     print(answer)

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# def bfs(info, x, y):
#     q = deque()
#     q.append((x,y))
#     while q:
#         now = q.popleft()
#         for i in range(4):
#             ny = now[0] + dy[i]
#             nx = now[1] + dx[i]
#             if 0 <= nx < m and 0 <= ny < n and info[ny][nx] == 1:
#                 info[ny][nx] = 0
#                 q.append((ny, nx))
# t = int(input())
#
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# for i in range(t):
#     m, n, k = map(int, input().split())
#     info = [[0]* m for _ in range(n)]
#     cnt = 0
#     for _ in range(k):
#         x, y = map(int, input().split())
#         info[y][x] = 1
#     for i in range(m):
#         for j in range(m):
#             if info[i][j] ==1:
#                 info[i][j] = 0
#                 bfs(info, i, j)
#                 cnt += 1
#     print(cnt)

import sys
from collections import deque

input = sys.stdin.readline

sys.setrecursionlimit(10**5)

def bfs(a,b):
    que = deque()
    que.append((a,b))
    graph[a][b] = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == -1:
                    que.append((nx, ny))
                    graph[nx][ny] = 1
    return

def dfs(x,y):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == -1:
                dfs(nx, ny)

    return

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = -1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1:

                dfs(i, j)
                cnt += 1
    print(cnt)

