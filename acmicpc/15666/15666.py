import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

n_list = list(map(int, input().split()))

n_list = sorted(list(set(n_list)))

for i in combinations_with_replacement(n_list, m):
    print(*i)
