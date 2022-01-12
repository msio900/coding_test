# import sys
# from math import factorial
#
# # n개의 원소를 가지는 집합에서 m개의 부분집합을 고르는 경우의 수
# n, m = map(int, sys.stdin.readline().split())
# print(f'n : {n} \nm : {m}')             # n과 m값 확인
#
# # (n, n-m)    분모
# # (1, m+1)    분자
# a = 1
# b = 1
# for i in reversed(range(n-m+1, n+1)):
#     print('첫번째',i,'*', a)
#     a = i * a
#
# for j in reversed(range(1, m+1)):
#     print('두번째',j,'*', b)
#     b = j * b
#
# answer = 0
# for i in reversed(str(int(a / b))):
#     if i == '0':
#         answer+=1
#     else:
#         break
#
# print(answer)

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
import sys


def countNum(N, num):
    count = 0
    divNum = num
    while( N >= divNum):
        count = count + (N // divNum)
        divNum = divNum * num
    return count

M, N = map(int, sys.stdin.readline().split())

print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))

