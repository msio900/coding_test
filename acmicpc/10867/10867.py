import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums = list(set(nums))
nums.sort()

print(*nums)