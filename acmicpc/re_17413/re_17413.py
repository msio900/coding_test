import sys

input = sys.stdin.readline

str_arr = list(map(str, input().rstrip()))
# print(str_arr)

answer = ''
i = 0
point = False
word = ''
for i in str_arr:
    if i == '<':
        point = True
        answer += word[::-1]
        answer += i
        word = ''
        # print(i)
        continue

    elif i == '>':
        point = False
        answer += i
        # print(i)
        continue
    elif i == ' ':
        answer += word[::-1]
        answer += i
        word = ''
        # print(i)
        continue

    if point:
        answer += i
    else:
        word += i

print(answer+word[::-1])