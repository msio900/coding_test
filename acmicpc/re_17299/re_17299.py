import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))


arr_cnt = Counter(arr)
# print(arr_cnt)

answer = [-1]*N
stack = []

stack.append(0)
for i in range(1, N):
    while stack and arr_cnt[arr[stack[-1]]] < arr_cnt[arr[i]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)