import sys

input = sys.stdin.readline
exp = input().rstrip()

answer = ''
opr_list = []
for i in exp:
    if i.isalpha():
        answer += i
    else:
        if i =='(':
            opr_list.append(i)
        elif i == '*' or i == '/':
            while opr_list and (opr_list[-1] == '*' or opr_list[-1] == '/'):
                answer += opr_list.pop()
            opr_list.append(i)
        elif i == '+' or i == '-':
            while opr_list and opr_list[-1] != '(':
                answer += opr_list.pop()
            opr_list.append(i)
        elif i == ')':
            while opr_list and opr_list[-1] != '(':
                answer += opr_list.pop()
            opr_list.pop()

while opr_list:
    answer += opr_list.pop()


print(answer)