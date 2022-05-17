import sys


input = sys.stdin.readline

laser = str(input().strip())
n = len(laser)

bar = []
for i in range(n-1):
    if laser[i] == '(' and laser[i+1] == ')':
        bar.append(laser[i]+laser[i+1])#, end='')
    if laser[i] == '(' and laser[i+1] == '(':
        bar.append('-') #, end='')
    if laser[i] == ')' and laser[i+1] == ')':
        bar.append('-') #, end='')
    if laser[i] == ')' and laser[i+1] == '(':
        bar.append('-') #, end='')

print(bar)


