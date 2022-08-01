import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
list = list(map(int, input().split()))

for i in list:
    answer = 0
    for j in nums:
        if i == j:
            answer += 1
    print(answer, end=' ')