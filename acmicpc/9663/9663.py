import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
s_list = list(map(int, input().split()))
answer = 0
for i in range(1, len(s_list)+1):
    for j in combinations(s_list, i):
        if sum(j) == s:
            answer += 1
print(answer)
