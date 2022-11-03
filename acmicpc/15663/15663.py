import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

n_list = list(map(int, input().split()))

cases = sorted(set(permutations(n_list, m)))

for case in cases:
    for j in case:
        print(j, end=' ')
    print()