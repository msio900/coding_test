import sys

input = sys.stdin.readline

n = int(input())
answer = 0
while n != 1:
    if n % 3 == 0:
        n //= 3
        answer += 1
    elif n % 2 == 0:
        n //= 2
        answer += 1
    else:
        n -=1
        answer += 1

print(answer)

