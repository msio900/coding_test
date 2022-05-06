# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for _ in range(T):
#     x = input().rstrip()
#     cnt = 0
#     com = 0
#     for i in x:
#         if i == '(':
#             cnt += 1
#         elif i == ')':
#             cnt -= 1
#             if cnt < 0:
#                 break
#
#     print('YES') if not cnt else print('NO')
