# N : 숨바꼭질을 함께하는 동생 수
# S : 수빈이가 현재 있는 위치
# 동생은 A1, A2, A3...An에 있음

import sys
from math import gcd

input = sys.stdin.readline

n, s = map(int, input().split())
brothers_position = list(map(int, input().split()))
if n != 1:
    ans = [gcd(abs(brothers_position[0] - s), abs(brothers_position[1] - s))]
    for i in range(2, n-1):
        ans[0] = gcd(ans[0], abs(brothers_position[i] - s))
else:
    ans = [abs(brothers_position[0]-s)]


print(*ans)