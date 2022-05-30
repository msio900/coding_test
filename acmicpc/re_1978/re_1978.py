import sys

N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
answer = N

for i in list:
    if i != 1:
        for j in range(2, i):
            print(f'{i} / {j} = {i % j}')
            if i % j == 0:
                answer -= 1
                break

    else:
        answer -= 1
print(answer)