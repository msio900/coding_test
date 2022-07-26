import sys

input = sys.stdin.readline

n = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_arr.sort()
b_arr.sort(reverse=True)
s = 0
for i in range(n):
    s+= a_arr[i]*b_arr[i]
print(s)