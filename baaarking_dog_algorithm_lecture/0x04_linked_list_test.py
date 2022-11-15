MX = 1000005
dat = [-1] * MX
pre = [-1] * MX
nxt = [-1] * MX

unused = 1

def insert(addr : int, num: int):
    global unused
    dat[unused] = num
    pre[unused] = addr
    nxt[unused] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = unused
    nxt[addr] = unused
    unused += 1

def traverse():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end=' ')
        cur = nxt[cur]
    print()

def erase(addr : int):
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1:
        pre[nxt[addr]] = pre[addr]


def insert_test():
    print('******* insert_test *******')
    insert(0, 10) # 10(address=1) <- 시작노드
    traverse()
    insert(0, 30) # 30(address=2) 10
    traverse()
    insert(2, 40) # 30 40(address=3) 10
    traverse()
    insert(1, 20) # 30 40 10 20(address=4)
    traverse()
    insert(4, 70) # 30 40 10 20 70(address=5)
    traverse()

def erase_test():
    print('******* erase_test *******')
    erase(1) # 30 40 20 70
    traverse()
    erase(2) # 40 20 70
    traverse()
    erase(4) # 40 70
    traverse()
    erase(5) # 40
    traverse()

insert_test()
erase_test()