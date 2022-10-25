import sys
from collections import defaultdict

# A - B, B - C, C - D, D - E친구관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

input = sys.stdin.readline

n, m = map(int, input().split())

relations = [[]for _ in range(n)]

visited = [False] * 2001

answer = False

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

def dfs(idx, depth):
    global answer
    visited[idx] = True
    if depth == 4:
        answer = True
        return
    for i in relations[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if answer:
        break
if answer:
    print(1)
else:
    print(0)
