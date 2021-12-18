import sys
import math

N = int(sys.stdin.readline())
expression = sys.stdin.readline().strip()
nums = [0]*N

for i in range(N):
    nums[i]=int(sys.stdin.readline())

# print(f'N : {N}\n str : {expression}\n nums : {nums}')

stack=[]

for i in expression:
    #문자이면
    if i.isupper():
        print(f'i가 문자일 경우 {i}')
        #nums[해당 문자의 아스키코드에 해당하는 index]
        stack.append(nums[ord(i)-ord('A')])
        print(f'i가 {i}일때, 스택은 {stack}')
    #연산자이면
    else:
        print(f'i가 연산자일 경우 {i}')
        #뒤에 추가된 숫자먼저 빼오고
        #이전에 추가된 숫자빼오기
        num2=stack.pop()
        print(num2)
        num1=stack.pop()
        print(num1)
        if i=='+':
            print(f'+에서 num1 : {num1}, num2 : {num2}')
            stack.append(num1+num2)
            print(f'스택은 {stack}')
        elif i=='-':
            print(f'-에서 num1 : {num1}, num2 : {num2}')
            stack.append(num1-num2)
            print(f'스택은 {stack}')
        elif i=='/':
            print(f'/에서 num1 : {num1}, num2 : {num2}')
            stack.append(num1/num2)
            print(f'스택은 {stack}')
        elif i=='*':
            print(f'*에서 num1 : {num1}, num2 : {num2}')
            stack.append(num1*num2)
            print(f'스택은 {stack}')
# #소수점 두자리까지 출력하는 방법
print(f"{stack[0]:.2f}")