import sys

input = sys.stdin.readline

mx = 10000005
dat = [0]*(2*mx+1)
head, tail = mx, mx

def push_front(x : int):
    global head
    head -= 1
    dat[head] = x

def push_back(x : int):
    global tail
    dat[tail] = x
    tail += 1

def pop_front() -> int:
    global head, tail
    if head == tail:
        return -1
    else:
        head += 1
        return dat[head-1]

def pop_back() -> int:
    global head, tail

    if head == tail:
        return -1
    else:
        tail -= 1
        return dat[tail]

def size() -> int:
    global head, tail

    return tail - head

def empty() -> int:
    global head, tail

    if head == tail:
        return 1
    else:
        return 0
def front() -> int:
    global head, tail

    if head == tail:
        return -1
    else:
        return dat[head]

def back() -> int:
    global head, tail

    if head == tail:
        return -1
    else:
        return dat[tail-1]

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'push_back':
        push_back(command[1])
    elif command[0] == 'push_front':
        push_front(command[1])
    elif command[0] == 'pop_front':
        print(pop_front())
    elif command[0] == 'pop_back':
        print(pop_back())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    else: # back
        print(back())