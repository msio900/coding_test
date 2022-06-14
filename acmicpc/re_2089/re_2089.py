import sys

input = sys.stdin.readline

n = int(input())

if not n:
    sys.stdout.write('0')
    exit()
answer = ''
while n != 0:
    if n < 0 and n + 1 != 0:
        a, b = divmod(n, -2)
        if b == 0:
            n = a
        else:
            n = a + 1
        answer += str(abs(b))
    else:
        a, b = divmod(n, -2)
        if b == 0:
            n = a
        else:
            n = a + 1
        answer += str(abs(b))

print(answer[::-1])
