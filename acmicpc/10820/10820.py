import sys

# |   소문자   |   대문자   |   숫자   |   공백   |의 갯수

while True:
    sentence = sys.stdin.readline()
    a, b, c, d = 0, 0, 0, 0
    print(sentence)

    if not sentence:
        break
    for i in sentence:
        if i.islower():
            a += 1
        elif i.isupper():
            b += 1
        elif ord('0') <= ord(i) <= ord('9'):
            c += 1
        elif i == ' ':
            d += 1
    print(a, b, c, d)