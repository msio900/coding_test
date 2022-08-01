import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
list = list(map(int, input().split()))

cnt_list = Counter(nums)
# print(cnt_list)

for i in list:
    if not cnt_list.get(i):
        print(0, end=' ')
    else:
        print(cnt_list.get(i), end=' ')