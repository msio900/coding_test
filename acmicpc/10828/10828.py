import sys

stack = []

N=int(sys.stdin.readline())

for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        stack.insert(0,word[1])

    if order =='pop':
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[0])
            stack.pop(0)

    if order =='size':
        print(len(stack))

    if order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if order == 'top':
        if len(stack) == 0:
            print(-1)
        else :
            print(stack[0])
