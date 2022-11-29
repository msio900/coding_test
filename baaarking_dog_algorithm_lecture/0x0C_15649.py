import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(range(1, n+1))
isused = [0] * n

def func(k : int):
    if k == m :
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, n + 1):
        if not isused[i-1]:
            arr[k] = i
            isused[i- 1] = 1
            func(k + 1)
            isused[i-1] = 0

func(0)