# 1번 집부터 n번 집까지 집이 순서대로 있음
# R G B 중 하나의 색으로 집을 칠해야함.
# 1번 집의 색은 2번 집의 색과 같지 않아야 함.
# n번 집의 색은 n-1번 집의 색과 같지 않아야함.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

import sys

input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n):
    costs = list(map(int, input().split()))
    print(costs, costs.index(min(costs)))
    k = costs.index(min(costs))
    answer += min(costs)

print(answer)
