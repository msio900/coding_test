import sys

N = int(sys.stdin.readline())
list = []
for _ in range(N):
    list.append(int(sys.stdin.readline()))

print(sorted(list, reverse=True))