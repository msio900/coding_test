import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

mx = 0
num = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 0 or visited[i][j]:
            continue
        num += 1
        queue = deque()
        visited[i][j] = True
        queue.append([i, j])
        area = 0
        while queue:
            area += 1
            cur = queue.popleft()
            for dir in range(4):

                nx = cur[0] + dx[dir]
                ny = cur[1] + dy[dir]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] or paper[nx][ny] != 1:
                    continue
                visited[nx][ny] = True
                queue.append([nx, ny])
        mx = max(mx, area)

print(num)
print(mx)
