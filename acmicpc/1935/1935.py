import sys

N = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip()

stack = []
operator = ['+','-','/','*']
o_list = []

for i in sentence:
    if i in operator:
        o_list.append(i)
for _ in range(N):
    stack.append(int(sys.stdin.readline()))
print(o_list)
print(stack)