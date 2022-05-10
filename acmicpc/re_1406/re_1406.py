import sys

input = sys.stdin.readline

L_stack = list(map(str, input().rstrip()))

M = int(input())

R_stack = []
# 커서의 위치는 명령어가 수행되기 전에는 맨 뒤에 위치하고 있음.
for _ in range(M):
    command = input().split()
    if command[0] == 'L' and len(L_stack) != 0:
        R_stack.append(L_stack.pop())
        # R_stack.insert(0, L_stack.pop())

    if command[0] == 'D'and len(R_stack) != 0:
        # print('D', command)
        L_stack.append(R_stack.pop())


    if command[0] == 'B' and len(L_stack) != 0:
        L_stack.pop()

    if command[0] == 'P':
        # print('P', command)
        L_stack.append(command[1])


R_stack.reverse()
print(''.join(L_stack+R_stack))