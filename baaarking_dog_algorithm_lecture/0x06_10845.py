import sys

mx = 1000005
dat = [0] * mx
head, tail = 0, 0

def push(x : int):
    global tail
    dat[tail] = x
    tail += 1

def pop() -> int:
    global head
    if tail != head:
        head += 1
        return dat[head - 1]
    else:
        return -1

def size() -> int:
    return tail - head

def empty() -> int:
    if tail != head:
        return 0
    else:
        return 1

def front() -> int:
    if tail != head:
        return dat[head]
    else:
        return -1

def back() -> int:
    if tail != head:
        return dat[tail - 1]
    else:
        return -1


input = sys.stdin.readline

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    else:
        print(back())