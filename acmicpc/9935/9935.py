import sys

input = sys.stdin.readline

str_arr = input().rstrip()
bomb = list(input().rstrip())


# print(1, str_arr)
stack = []

for i in range(len(str_arr)):
    stack.append(str_arr[i])

    if len(stack) >= len(bomb) and stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')