# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# n = 1000001
# a = [False,False] + [True]*(n-1)
# primes=[]
# # 에라토스테네스의 체를 이용하여 n까지의 소수를 구함
# for i in range(2, n+1):
#     if a[i]:
#         primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
#
# while True :
#     t = int(input())
#     if t == 0:
#         break
#     flag = True
#     pt = 0
#     while True:
#         if primes[pt] >= t:
#             break
#         pt += 1
#     p_list = primes[:pt]
#     for i in p_list:
#         if t - i
#         print()
#
#
#
#     if flag:
#         print("Goldbach's conjecture is wrong.")
import sys

input = sys.stdin.readline

chk = [True for i in range(1000001)]

for i in range(2,1001):
    if chk[i]:
        for j in range(i*2, 1000001, i):
            chk[j] = False

while True:
    n = int(input())
    if n == 0 :
        break
    for i in range(3, len(chk)):
        if chk[i] and chk[n-i]:
            print(n, "=", i, "+", n - i)
            break
