# import sys
#
# # in[0]
# # 2
# # 1 3
# # 1
# # out[0]
# # 0.5
#
# N = int(sys.stdin.readline())
# cake_gram = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
#
# dif = []
# dif.append(float(max(cake_gram)-min(cake_gram)))
# for _ in range(M):
#     cake_gram.sort(reverse=True)
#     a = cake_gram.pop(0)/2
#     cake_gram.append(a)
#     dif.append(float(max(cake_gram)-min(cake_gram)))
# print(min(dif))

# 류호석님 시간초과
import sys

si = sys.stdin.readline
N = int(si())
a = list(map(int, si().split()))
a = [(x, 0)for x in a]
M = int(si())

ans = max(a)[0] - min(a)[0]

for _ in range(M):
    # 제일 큰 조각 찾기
    sz, idx = a[0][0], 0
    for i in range(1, N):
        if sz < a[i][0]:
            sz, idx = a[i][0], i

    # 제일 큰 조각에 칼질 한 번 더 하기
    org_sz = (a[idx][0] * (a[idx][1] + 1))  # 원래 사이즈 = 조각 크기 * 조각 개수(=자른 횟수 + 1)
    a[idx] = (org_sz / (a[idx][1] + 2), a[idx][1] + 1)

    # 정답 갱신
    ans = min(ans, max(a)[0] - min(a)[0])
print(float(ans))

