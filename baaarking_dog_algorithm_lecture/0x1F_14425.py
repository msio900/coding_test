import sys

input = sys.stdin.readline

ROOT = 1
unused = 2
MX = 10000 * 500 + 5
chk = [False] * MX
nxt = [[] * MX for _ in range(26)]

def c2i(c: str):
    return c - 'a'

def insert(s: str):
    global unused
    cur = ROOT
    for c in s:
        if nxt[cur][c2i(c)] == -1:
            nxt[cur][c2i(c)] = unused
            unused += 1
    chk[cur] = True

def find(s: str)->bool:
    cur = ROOT
    for c in s:
        if nxt[cur][c2i(c)] == -1:
            return False
        cur = nxt[cur][c2i(c)]

    return chk[cur]

