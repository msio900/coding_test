# import sys
# from itertools import combinations_with_replacement
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# n_list = list(map(int, input().split()))
#
# n_list = sorted(list(set(n_list)))
#
# for i in combinations_with_replacement(n_list, m):
#     print(*i)

def backTracking(seq, cnt):
    cnt -= 1
    if cnt == -1:
        print(*seq)
        return
    for i in arr:
        if not seq or i >= seq[-1]:
            backTracking(seq+[i], cnt)

n, m = 4, 2
arr = sorted(list(set([9,7,9,1])))

print(backTracking([], m))

