import sys


# 스택을 구현하는 문제
input = sys.stdin.readline
N = int(input())

stack = []
for _ in range(N):
    order = input().split()
    command = order[0].rstrip()
    if len(order) == 2:
        X = order[1].rstrip()
    if command == 'push':
       stack.append(X)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

