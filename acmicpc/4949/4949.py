import sys

input = sys.stdin.readline
s = []
while True:
    if input().rstrip() == '.':
        break
    s.append(input().rstrip())
    print(s)