mx = 1000005
dat = [0]*mx
head, tail = 0, 0

def push(x : int):
    global tail
    dat[tail] = x
    tail += 1

def pop():
    global head
    head += 1

def front() -> int:
    return dat[head]

def back() -> int:
    return dat[tail-1]

push(1)
print(front(), back())
push(2)
print(front(), back())
push(3)
print(front(), back())
push(4)
pop()
print(front(), back())
pop()
push(5)
push(6)
push(7)
print(front(), back())

