import sys
from math import gcd
from itertools import combinations

t = int(sys.stdin.readline())

for _ in range(t):
    n_list = list(map(int, sys.stdin.readline().split()))
    n = n_list.pop(0)
    a = []
    for i in combinations(n_list, 2):
      a.append(gcd(i[0], i[1]))
    print(sum(a))

