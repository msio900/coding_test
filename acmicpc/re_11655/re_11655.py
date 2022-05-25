import sys

input = sys.stdin.readline

S = input()

answer = ''
# print(ord('A')- ord('Z'))
# print(ord('Z'))
for i in S:
    if i.isupper():
        if ord('A') <= ord(i) + 13 <= ord('Z'):
            answer += chr(ord(i) + 13)
            # print('범주 안', i)
        else:
            answer += chr((ord(i) + 13) - 26)

    elif i.islower():
        if ord('a') <= ord(i) + 13 <= ord('z'):
            answer += chr(ord(i) + 13)
            # print('범주 안', i)
        else:
            answer += chr((ord(i) + 13) - 26)
    else:
        answer += i

print(answer)