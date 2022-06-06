import sys

input = sys.stdin.readline

N = int(input())

ans = 1
for i in range(1,N+1):
    ans *= i

cnt = 0
for j in str(ans)[::-1]:
    if j == '0':
        cnt+=1
        # print(j)
    else :
        break
print(cnt)