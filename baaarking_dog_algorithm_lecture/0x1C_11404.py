import sys

input = sys.stdin.readline

n = int(input())
matrix = [[100000000]*n for _ in range(n)]

for _ in range(int(input())):
    x, y, cost = map(int, input().split())
    matrix[x-1][y-1] = min(matrix[x-1][y-1], cost)

for i in range(n):
    matrix[i][i] = 0


for s in range(n):
    for i in range(n):
        for j in range(n):
            if i != s or j != s:
                matrix[i][j] = min(matrix[i][s]+matrix[s][j], matrix[i][j])

for i in range(n):
    for j in range(n):
        print(0 if matrix[i][j] == 100000000 else matrix[i][j], end=' ')
    print()