import sys

input = sys.stdin.readline

N = int(input())
list = list(map(int, input().split()))
answer = N

for i in list:
    if i != 1:
        for j in range(2, i):
            # print(f'{i} / {j} = {i % j}')
            if i % j == 0:
                answer -= 1
                break

    else:
        answer -= 1
print(answer)