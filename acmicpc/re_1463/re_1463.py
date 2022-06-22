# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# answer = 0
# while n != 1:
#     if n % 3 == 0:
#         n //= 3
#         answer += 1
#     elif n % 2 == 0:
#         n //= 2
#         answer += 1
#     else:
#         n -=1
#         answer += 1
#
# print(answer)

import sys

input = sys.stdin.readline


X = int(input())

dp = [0 for _ in range(X + 1)]

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[X])


# s = {1:0, 2:1}
#
# def f(n):
#     if n in s :
#         return s[n]
#     m = 1 + min(f(n // 2) + n % 2, f(n // 3) + n % 3)
#     s[n] = m
#     return m
#
# print(f(int(input())))

# l = {int(input())}
# n = 0
#
# while 1 not in l:
#     t = set()
#     n += 1
#     for i in l:
#         if i % 3 == 0:
#             t.add(i // 3)
#         if i % 2 == 0:
#             t.add(i // 2)
#         t.add(i - 1)
#     l = t
# print(n)
