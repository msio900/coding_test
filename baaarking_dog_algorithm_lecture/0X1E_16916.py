import sys

input = sys.stdin.readline

def failure(s: str) -> list[int]:
    f = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]
        if s[i] == s[j]:
            j += 1
            f[i] = j
    return f

s = input().rstrip()
p = input().rstrip()

f = failure(p)
j = 0
for i in range(len(s)):
    while j > 0 and s[i] != p[j]:
        j = f[j - 1]
    if s[i] == p[j]:
        j += 1
    if j == len(p):
        print(1)
        break
else:
    print(0)