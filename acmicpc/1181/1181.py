import sys

input = sys.stdin.readline

n = int(input())
s = [input().rstrip() for _ in range(n)]
s = list(set(s))
s.sort()
s.sort(key=lambda i:len(i))

for i in s:
    print(i)