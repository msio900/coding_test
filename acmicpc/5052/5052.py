import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # n : 전화번호의 수
    n = int(input())
    num_list = [input().rstrip() for i in range(n)]
    num_list.sort()
    # print(num_list)
    for i in range(n-1):
        if num_list[i] == num_list[i+1][:len(num_list[i])]:
            print('NO')
            break
    else :
        print('YES')