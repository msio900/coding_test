# 대회는 정확히 3명으로 구성된 팀만 참가가 가능함
# -10000 < Aj < 10000
# 합이 0이 되는 팀을 만들고자 함
import sys
from itertools import combinations
from typing import List


input = sys.stdin.readline

N = int(input())

A_list = sorted(list(map(int, input().split())))
print(A_list)

target = 0
# 투포인터

for i in range(N-2):
    left, right = i + 1, len(A_list) - 1
    while not left == right:
        if A_list[i] + A_list[left] + A_list[right] < target:
            left += 1
        elif A_list[i] + A_list[left] + A_list[right] > target:
            right -= 1
        elif A_list[i] + A_list[left] + A_list[right] == target:
            print(A_list[i], A_list[left], A_list[right])






# itertools 활용
# # cnt = 0
# # for i in combinations(A_list, 3):
# #     # print(i)
# #     if sum(i) == 0:
# #         cnt += 1
# #
# # print(cnt)
#
# print(A_list)

## 이진 탐색
# def twoSum(numbers : List[int], target : int) -> List[int]:
#     cnt_1 = 0
#     for k, v in enumerate(numbers):
#         cnt_2 = 0
#         left, right = k + 1, len(numbers) - 1
#         expected = target - v
#         cnt_1 += 1
#         print('cnt_1', cnt_1)
#         while left <= right:
#             cnt_2 += 1
#             print('cnt_2', cnt_2)
#             mid = left +(right - left)//2
#             if numbers[mid] < expected:
#                 left = mid + 1
#             elif numbers[mid] > expected:
#                 right = mid - 1
#             else:
#                 return k + 1, mid + 1
#
# print(twoSum(A_list, 0))
