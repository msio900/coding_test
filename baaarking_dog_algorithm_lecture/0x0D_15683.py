import sys

input = sys.stdin.readline

n, m = map(int, input().split())
office_info = [list(map(int, input().split())) for _ in range(n)]

# 4진수 출력하는 법
# for tmp in range(64):
#     brute = tmp
#     for i in range(3):
#         print(brute % 4, end='')
#         brute //= 4
#     print()



# 1. CCTV가 있는 좌표와 벽이 있는 좌표를 찾는다.

# coordinate = []
# for i in range(n):
#     for j in range(m):
#         if office_info[i][j]:
#             coordinate.append([office_info[i][j], i, j])
# 2. 각 CCTV가 감시하는 방향의 경우의 수마다 사각지대의 개수를 구한다.



# 3. 사각지대 개수의 최소값을 출력한다.

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def OOB(a : int, b : int):
    return a < 0 or a >= n or b < 0 or b >= m

def upd(x : int, y : int, dir : int):
    dir %= 4
    while 1:
        x += dx[dir]
        y += dy[dir]
        if OOB(x, y) or office_info[x][y] ==6:
            return
        if office_info[x][y] != 0:
            continue
        office_info[x][y] = 7

mn = 0
coordinate = []
for i in range(n):
    for j in range(m):
        if office_info[i][j]:
            coordinate.append([i, j])
for tmp in range()



