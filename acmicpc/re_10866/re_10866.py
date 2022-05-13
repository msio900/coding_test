import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

que = deque()

for _ in range(N):
    order = input().split()
    if order[0] == 'push_front':
        que.appendleft(order[1])
    if order[0] == 'push_back':
        que.append(order[1])
    if order[0] == 'pop_front':
        print(que.popleft() if que else -1)
    if order[0] == 'pop_back':
        print(que.pop() if que else -1)
    if order[0] == 'size':
        print(len(que))
    if order[0] == 'empty':
        print(0 if que else 1)
    if order[0] == 'front':
        print(que[0] if que else -1)
    if order[0] == 'back':
        print(que[-1] if que else -1)
