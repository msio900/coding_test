import sys
from itertools import combinations

input = sys.stdin.readline

while True: # break가 나올 때까지
    l = list(map(int, input().split()))
    if l[0] == 0: # 반복문 break조건
        break
    else:
        s = l[1:]
        for i in combinations(s, 6): # 주어진 수 중 6개를 뽑는 조합
            i = list(i)
            print(*i)
        print( )