# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n, k = map(int, input().rstrip().split())
#
# que = deque()
#
# for i in range(1, n+1):
#     que.append(i)
# answer = []
#
# while que:
#     for i in range(k-1):
#         que.append(que.popleft())
#     answer.append(str(que.popleft()))
#
# answer = ', '.join(answer)
# print(f"<{answer}>")



import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())


circle_list = [i for i in range(1, n+1)]
remove_list = []

idx = 0
for i in range(n):
    idx += k - 1
    if idx >= len(circle_list):
        idx = idx % len(circle_list)
    remove_list.append(str(circle_list.pop(idx)))

print(f'<{", ".join(remove_list)}>')