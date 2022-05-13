# 대회는 정확히 3명으로 구성된 팀만 참가가 가능함
# -10000 < Aj < 10000
# 합이 0이 되는 팀을 만들고자 함
import sys

input = sys.stdin.readline

N = int(input())

A_list = list(map(int, input().split()))
cnt = 0
print(A_list)


# 이진 검색
List = []
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        left, right = k + 1, len(numbers) - 1
        expected = target - v
        while left <= right:
            mid = left + (right - left) //2
            if numbers[mid] < expected:
                left = mid +1
            elif numbers[mid] > expected:
                right = mid -1
            else:
                return k + 1, mid + 1

print(twoSum(A_list, cnt))