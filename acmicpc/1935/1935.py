import sys



N = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip()

stack = []
operator = ['+','-','/','*']

for i in sentence:
    if i in operator:
        stack.append(i)
print(stack)