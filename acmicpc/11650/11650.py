import sys

input = sys.stdin.readline

n = int(input())

coordinates = [list(map(int, input().split())) for _ in range(n)]
coordinates.sort(key=lambda x : (x[0], x[1]))

for i in coordinates:
    print(*i)