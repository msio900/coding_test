import sys

input = sys.stdin.readline

# 1부터 n까지의 수
n = int(input())
n_list = [i for i in range(1, n+1)]
# 4 3 6 6 7 5 2 1

stack = []
current_num = 1
answer = []
flag = 0

for i in range(n):
    num = int(input())
    while current_num <= num :
        stack.append(current_num)
        answer.append('+')
        current_num += 1

    if stack[-1] == num :
        stack.pop()
        answer.append('-')

    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)

