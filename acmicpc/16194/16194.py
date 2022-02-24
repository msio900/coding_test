import sys


N = int(sys.stdin.readline())

d = [0] * (N + 1)
p = [0] + list(map(int, sys.stdin.readline().split()))
d[1] = p[1]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        if d[i] < d[i - j] + p[j]:
            d[i] = d[i - j] + p[j]
print(d[N])