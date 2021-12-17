import sys

N = int(sys.stdin.readline())
sentence = [i for i in sys.stdin.readline().strip()]
operator = ['+', '-', '*', '/']
unique_stk = []

for i in range(len(sentence)):
    if sentence[i] not in operator:
        unique_stk.append(sentence[i])

unique_stk = list(set(unique_stk))
unique_stk.sort()
print(unique_stk)
for i in range(N):
    unique_stk[i] = int(sys.stdin.readline())

print(unique_stk)