import sys

input = sys.stdin.readline

n = int(input())
dy = [0]*1001
dy[1]=1
dy[2]=3
for i in range(3,n+1):
    dy[i] = (dy[i - 1] + dy[i - 2] * 2)%10007

print(dy[n])