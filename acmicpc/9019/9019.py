# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
# 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
# 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
# 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = input().split()



    print(a, b)

from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    q = deque()
    q.append((A, ""))
    visit = [False] * 10000

    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break

        # 1
        num2 = (2 * num) % 10000
        if not visit[num2]:
            q.append((num2, path + "D"))
            visit[num2] = True
        # 2
        num2 = (num - 1) % 10000
        if not visit[num2]:
            q.append((num2, path + "S"))
            visit[num2] = True
        # 3
        num2 = (10 * num + (num // 1000)) % 10000
        if not visit[num2]:
            q.append((num2, path + "L"))
            visit[num2] = True

        # 4
        num2 = (num // 10 + (num % 10) * 1000) % 10000
        if not visit[num2]:
            q.append((num2, path + "R"))
            visit[num2] = True