import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

que = deque()

for i in range(1, n+1):
    que.append(i)
answer = []

while que:
    for i in range(k-1):
        que.append(que.popleft())
    answer.append(str(que.popleft()))

answer = ', '.join(answer)
print(f"<{answer}>")