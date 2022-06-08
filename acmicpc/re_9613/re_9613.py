import sys
from itertools import combinations
from math import gcd

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))[1:]
    print(nums)
    ans = 0
    for i in combinations(nums, 2):
        ans += gcd(i[0], i[1])

    print(ans)