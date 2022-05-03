# N = 빌딩의 개수
# 다른 빌딩의 옥상 정원을 벤치마킹 하고 싶어진다.
# i 번째 빌딩의 키가 hi이고, 모든 빌딩은 일렬로 서 있고 오른쪽만 볼 수 있다.
# i 번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+1 i+2 ... N이다.
# if i번째 빌딩의 높이 <= k 의 높이 이라면 그 다음에 있는 빌딩의 옥상은 보지 못함.

import sys

input = sys.stdin.readline

N = int(input())

hi = [int(input()) for _ in range(N)]
# print(hi)

cnt = 0
stack = []
for i in range(N):
    while stack and stack[-1] <= hi[i]:
        stack.pop()
    stack.append(hi[i])
    cnt += len(stack) - 1
    # for j in range(i+1, N):
    #     if hi[i] <= hi[j]:
    #         # print(cnt)
    #         break
    #     else:
    #         cnt += 1

print(cnt)