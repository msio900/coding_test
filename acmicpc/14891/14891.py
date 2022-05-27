import sys

input = sys.stdin.readline

S  = input().rstrip()

array = []
for i in range(len(S)):
    array.append(S[i:])

array.sort()
# print(array)
for i in array:
    print(i)

