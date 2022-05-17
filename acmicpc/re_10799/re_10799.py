import sys


input = sys.stdin.readline

laser = str(input().strip())
n = len(laser)

cut_bar = laser.replace('()', '*')
print(cut_bar)

bar = []
answer = 0
for i in cut_bar:
    if i == '(':
        bar.append(i)
    if i == '*':
        answer += len(bar)
    if i == ')':
        bar.pop()
        answer += 1
print(answer)
