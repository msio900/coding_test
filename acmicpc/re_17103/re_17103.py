import sys
from itertools import permutations

# 골드바흐의 추측 : 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
input = sys.stdin.readline

T = int(input())

max_num = 1000000
a = [False,False] + [True]*(max_num-1)
primes=[]

for i in range(2, max_num+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, max_num+1, i):
        a[j] = False

for _ in range(T):
    N = int(input())
    position = primes.index([i for i in primes if i <= N][-1])
    answer = 0
    print(primes[:position])
    for i in range(position):
        if primes[i] + primes[position - i - 1] == N:
            answer += 1
        if 2 * primes[i] == N:
            answer += 1
    print(answer)