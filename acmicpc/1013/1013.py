import sys

input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))
print(num)

# 2*17**1 + 16*17**0
to_ten = 0
for i in range(m):
    to_ten += num[i]*a**(m - i - 1)

print(to_ten)
answer = []
while to_ten != 0:
    c, d = divmod(to_ten, b)
    to_ten = c
    answer.append(str(d))
print(' '.join(answer[::-1]))
