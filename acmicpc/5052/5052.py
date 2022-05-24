import sys

input = sys.stdin.readline

# t : 테스트 케이스
t = int(input())

for _ in range(t):
    # n : 전화번호의 수
    n = int(input())
    num_list = [input().rstrip() for i in range(n)]
    # print(num_list)
    bool = True
    for i in range(n):
        for j in range(i + 1, n):
            if num_list[i] == num_list[j][:len(num_list[i])]:
                bool = False
                print('NO')
                break
    if bool:
        print('YES')