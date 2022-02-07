import sys

N = int(sys.stdin.readline())
list = []
for _ in range(N):
    list.append(str(sys.stdin.readline().rstrip()))
list = sorted(list, reverse=True)
print(' '.join(list))