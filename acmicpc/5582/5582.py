import sys

input = sys.stdin.readline


while True:
    S = input()

    if not S:
        break
    a, b, c, d = 0, 0, 0, 0
    for i in S:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif i.isdigit():
            c += 1
        elif i == ' ':
            d += 1
    print(a, b, c, d)

