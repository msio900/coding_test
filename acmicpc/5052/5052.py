import sys

input = sys.stdin.readline

str_arr = input().rstrip()
# print(ord('a'))
answer = [-1]*(ord('z') - ord('a') + 1)

for i in reversed(range(len(str_arr))):
    answer[ord(str_arr[i])-97] = i

print(*answer)