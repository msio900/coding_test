import sys

input = sys.stdin.readline

s = input().rstrip()
n = int(input())

mx =1000005
dat = [-1]*mx
pre = [-1]*mx
nxt = [-1]*mx
unused = 1

def insert(addr:int, num:int):
    global unused
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def erase(addr:int):
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]

def traverse():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end='')
        cur = nxt[cur]
    print()
cursor = 0
for i in s:
    insert(cursor, i)
    cursor +=1

for _ in range(n):
    command = input().split()
    if command[0] == 'L':
        if pre[cursor] != -1:
            cursor = pre[cursor]
    elif command[0] == 'D':
        if nxt[cursor] != -1:
            cursor = nxt[cursor]
    elif command[0] == 'B':
        erase(cursor)
        cursor = pre[cursor]
    else:
        insert(cursor, command[1])
        cursor = nxt[cursor]
traverse()