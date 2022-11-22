import sys

input = sys.stdin.readline

while True:
    a = input().rstrip()
    if a == '.':
        break
    s = []
    is_valid = True
    for c in a:
        if c == '(' or c =='[':
            s.append(c)
        elif c == ')':
            if not s or s[-1] != '(':
                is_valid = False
                break
            s.pop()
        elif c == ']':
            if not s or s[-1] != '[':
                is_valid = False
                break
            s.pop()
    if s:
        is_valid = False
    if is_valid:
        print('yes')
    else:
        print('no')