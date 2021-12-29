import sys

S = list(map(str, sys.stdin.readline().rstrip()))

answer = []
for i in range(len(S)):
    answer.append(''.join(S[i:]))
answer.sort()
for i in answer:
    print(i)

