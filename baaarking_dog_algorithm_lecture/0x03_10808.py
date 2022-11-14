import sys

input = sys.stdin.readline

answer = [0] * 26
S = input().rstrip()

for i in S:
    answer[ord(i) - 97] += 1

print(*answer)

