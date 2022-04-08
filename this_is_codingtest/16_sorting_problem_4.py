# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# soldiers = list(map(int, input().split()))
#
# soldiers.reverse()
#
# dp = [1]*N
#
# for i in range(1, N):
#     for j in range(0, i):
#         if soldiers[j] < soldiers[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(N - max(dp))

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# soldiers = list(map(int, input().split()))
#
# soldiers.reverse()
#
# diff = []
# for i in range(N-1):
#     diff.append(soldiers[i] - soldiers[i+1])
# print(soldiers)
# print(diff)

for i in range(100, 1, -2):
    print(i)