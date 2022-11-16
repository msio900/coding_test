import sys

input = sys.stdin.readline

mx = 10000005
dat = [0]*mx
pos = 0

def push(x: int):
    global pos
    dat[pos] = x
    pos += 1

def pop():
    global pos
    pos -= 1


def size():
    return pos

def top():
    return dat[pos - 1]

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        if pos == 0:
            print(-1)
        else:
            print(top())
            pop()
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        if pos == 0:
            print(1)
        else:
            print(0)
    else: # top()
        if pos == 0:
            print(-1)
        else:
            print(top())
