MX = 1000005
dat = [0] * MX
pos = 0

def push(x : int):
    global pos
    dat[pos] = x
    pos += 1

def pop():
    global pos
    pos -= 1

def top():
    return dat[pos-1]

push(1)
print(top())
push(2)
print(top())
pop()
print(top())

push(3)
print(top())

push(4)
push(5)
push(6)
print(top())
pop()
print(top())
