import sys

N = int(sys.stdin.readline())

queue = []

for _ in range(N):
    input = sys.stdin.readline().split()
    command = input[0]
    if command == 'push':   # push X : 정수 X를 큐에 넣는 연산이다.
        queue.append(input[1])
        
    if command == 'pop':    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    if command == 'size':   # size: 큐에 들어있는 정수의 개수를 출력한다.
        print(len(queue))
    
    if command == 'empty':  # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    if command == 'front':  # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if command == 'back':   # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
