import sys


def countNum(N, num):
    count = 0
    divNum = num
    while( N >= divNum):
        count = count + (N // divNum)
        divNum = divNum * num
    return count

M, N = map(int, sys.stdin.readline().split())

print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))
