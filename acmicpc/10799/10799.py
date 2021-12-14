import sys

input = str(sys.stdin.readline().strip())
cut = 0
for i in range(len(input)-1):
    if (input[i] == '(') & (input[i+1] == ')'):
        cut += 1
        print(f'절단 {cut}회')
    elif (input[i] == '(') & (input[i+1] == '('):
        cut += 1
        print(f'절단 {cut}회')