# 대회는 정확히 3명으로 구성된 팀만 참가가 가능함
# -10000 < Aj < 10000
# 합이 0이 되는 팀을 만들고자 함
import sys
from itertools import combinations
from typing import List


# input = sys.stdin.readline
#
# N = int(input())
#
# A_list = list(map(int, input().split()))
#
# # cnt = 0
# # for i in combinations(A_list, 3):
# #     # print(i)
# #     if sum(i) == 0:
# #         cnt += 1
# #
# # print(cnt)
#
# print(A_list)

numbers = [2, 7, 11, 15]
target = 9
def twoSum(self, numbers: list[int], target : int) -> List[int]:
    for k, v in enumerate(numbers):
        left, right = k + 1, len(numbers) - 1
        expected = target - v
        while left <= right:
            mid = left +(right - left)//2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return k + 1, mid + 1

print(twoSum(numbers, target))
