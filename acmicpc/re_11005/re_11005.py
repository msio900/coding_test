import sys

input = sys.stdin.readline

n, b = map(int, input().split())
answer = ''
while n != 0:
    x, y = divmod(n, b)
    n = x
    if y <=9:
        # print(y)
        answer += str(y)
    else:
        # print(chr((y - 10) + ord('A')))
        answer += chr((y - 10) + ord('A'))

print(answer[::-1])