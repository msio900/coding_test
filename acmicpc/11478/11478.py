# import sys
#
# input = sys.stdin.readline
#
# M, N = map(int, input().split())
#
# def isPrime(a):
#   if(a<2):
#     return False
#   for i in range(2,a):
#     if(a%i==0):
#       return False
#   return True
#
# for i in range(M, N + 1):
#   if(isPrime(i)):
#     print(i)


import sys

input = sys.stdin.readline

M, N = map(int, input().split())

a = [False,False] + [True]*(N-1)
primes=[]

for i in range(2, N+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False

# print(primes)

for i in primes:
    if M <= i <=N:
        print(i)