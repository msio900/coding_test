import sys

expression = list(map(str, sys.stdin.readline().strip()))


operator = []

for i in range(len(expression)):
    print(expression)
    if expression: 
        expression.append(expression.pop(i))


print(expression)


## 