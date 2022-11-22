import sys

input = sys.stdin.readline

bracket = {'(':')', '[':']'}

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break
    stack = []
    flag = True
    for letter in sentence:
        if letter in '([':
            stack.append(letter)
        elif letter in ')]':
            if not stack:
                flag = False
                break
            elif stack:
                if bracket[stack[-1]] != letter:
                    flag = False
                    break
                elif bracket[stack[-1]] == letter:
                    stack.pop()
    if stack:
        flag = False
    if flag:
        print('yes')
    else:
        print('no')

