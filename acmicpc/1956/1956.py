import sys

input = sys.stdin.readline

# # 에라토스테네스의 체
# n = 10100
# a = [False,False] + [True]*(n-1)
# primes = []
#
# for i in range(2, n+1):
#     if a[i]:
#         primes.append(i)
#         for j in range(2*i, n+1, i):
#             a[j] = False
#
# # 비밀키 pq : 특정 소수 p와 q의 곱
#
# p, k = map(int, input().split())
#
# for i in primes:
#     if p % i == 0:
#         num = i
#         break
#
# if num <= k:
#     print('BAD', num)
# else:
#     print('GOOD')

p, k = map(int, input().split())

for i in range(2, k):
    if p % i == 0:
        print('BAD', i)
        break
else:
    print('GOOD')


