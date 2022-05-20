import sys

input = sys.stdin.readline
N = int(input())

exp = input()

nums = [int(input()) for i in range(N)]

print(N, exp, nums)

stack = []
for i in range(len(exp)):
    if 65 <= ord(exp[i]) <=90:
        stack.append(nums[ord(exp[i])-65])
    if exp[i] == '*':
        stack.append(stack.pop() * stack.pop())
    if exp[i] == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    if exp[i] == '+':
        stack.append(stack.pop() + stack.pop())
    if exp[i] == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
# answer = stack[0]
print(f"{stack[0]:.2f}")