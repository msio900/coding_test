import sys

# N : 진법을 바꾸고자 하는 수, B : 원하는 진법
N, B = map(int, sys.stdin.readline().rstrip().split())

num = []
while N != 0:# !=0
    if N % B < 10:
        num.append(str(N % B))
    else:
        num.append(chr(55 + N % B))
    N = N // B

answer = ''.join(num[::-1])

print(answer)