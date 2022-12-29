import sys

input = sys.stdin.readline

ROOT = 1
unused = 2
MX = 10000 * 500 + 5
chk = [False] * MX
nxt = [[-1] * 26 for _ in range(MX)]

def c2i(c: str):
    return ord(c) - ord('a')

def insert(s: str):
    global unused, ROOT
    cur = ROOT
    for c in s:
        if nxt[cur][c2i(c)] == -1:
            nxt[cur][c2i(c)] = unused
            unused += 1
        cur = nxt[cur][c2i(c)]
    chk[cur] = True

def find(s: str)->bool:
    cur = ROOT
    for c in s:
        if nxt[cur][c2i(c)] == -1:
            return False
        cur = nxt[cur][c2i(c)]
    return chk[cur]

n, m = map(int, input().split())

for _ in range(n):
    s = input().rstrip()
    insert(s)

answer = 0

for _ in range(m):
    s = input().rstrip()
    answer += find(s)

print(answer)

