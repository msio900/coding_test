import sys
from collections import Counter

input = sys.stdin.readline

str_arr = input().rstrip()

str_arr_cnt = Counter(str_arr)

answer = [0 for i in range(97,123)]
# print(answer)
# print(str_arr_cnt)
for k in str_arr_cnt:
    answer[ord(k)-97] = str_arr_cnt.get(k)

print(*answer)
