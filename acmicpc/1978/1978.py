import sys

T = int(sys.stdin.readline())

def GCD(A, B):
    while (B!=0):
        A = A % B
        A, B = B, A
    return A

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())


    print(int((A * B) / GCD(A, B)))