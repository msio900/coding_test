# import sys
#
# # 오일러 파이
#
# input = sys.stdin.readline
#
# n = 1
# while True:
#     n = int(input())
#     if n == 0:
#         print(n)
#         break

while 1:
    n = int(input())
    if n == 0:
        break
    tmp = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            tmp = tmp/i * (i-1)
        while n % i == 0:
            n = n/i
        i += 1
    if n != 1:
        tmp = tmp / n * (n-1)
    print(int(tmp))