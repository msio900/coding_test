import sys
from math import factorial

# n개의 원소를 가지는 집합에서 m개의 부분집합을 고르는 경우의 수
n, m = map(int, sys.stdin.readline().split())
print(f'n : {n} \nm : {m}')

print(f'n! : {factorial(n)}\nm! : {factorial(m)}\n(n-m)! : {factorial(n-m)}')
a = int(factorial(n) / factorial(m) / factorial((n-m)))
print(a)
answer = 0
for i in reversed(str(a)):
    if i == '0':
        answer+=1
    else:
        break

print(answer)

# import sys
# from math import factorial
# n, m = map(int, sys.stdin.readline().split())
# a = int(factorial(n) / factorial(m) / factorial((n-m)))
#
# answer = 0
# for i in reversed(str(a)):
#     if i == '0':
#         answer+=1
#     else:
#         break
#
# print(answer)