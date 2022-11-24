import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

def multiple(b : int, c: int) -> int:
    global a
    if b == 0:
        return a % c
    else:
        a *= a
        multiple(b - 1, c)
        print()

print(multiple(b, c))