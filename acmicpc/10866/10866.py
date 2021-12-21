import sys

N = int(sys.stdin.readline())

deque = []
for _ in range(N):
    input = sys.stdin.readline().split()
    command = input[0]

    # push_front X: 정수 X를 덱의 앞에 넣는다.
    if command == 'push_front':
        deque.insert(0, input[1])
    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif command == 'push_back':
        deque.insert(-1, input[1])
    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == 'pop_front':
        if len(deque) ==0:
            print(-1)
        else:
            print(deque.pop(0))
    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == 'pop_back':
        if len(deque) ==0:
            print(-1)
        else:
            print(deque.pop())
    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif command == 'size':
        print(len(deque))
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif command == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
