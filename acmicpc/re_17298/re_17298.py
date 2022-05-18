import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

## 이중 반복문 - 시간초과
# for i in range(len(nums)-1):
#     j = i+1
#     point = True
#     while j < len(nums):
#         if nums[i] < nums[j]:
#             print(nums[j], end=' ')
#             point = False
#             break
#         j += 1
#     if point:
#         print(-1, end=' ')
#
#
# print(-1)

# 스택을 이용한 풀이
answer = [-1]*N
stack = []
stack.append(0)
for i, j in enumerate(nums):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
