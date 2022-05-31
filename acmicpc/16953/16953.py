import sys

input = sys.stdin.readline

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.

A, B = map(int, input().split())
cnt = 1
while B != A:
    cnt += 1
    temp = B
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B//=2
    if temp == B:
        print(-1)
        break
else:
    print(cnt)