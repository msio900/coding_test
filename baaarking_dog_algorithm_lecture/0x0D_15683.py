import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

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



def OOB(a : int, b : int):
    return a < 0 or a >= n or b < 0 or b >= m

def upd(x : int, y : int, dir : int):
    dir %= 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if OOB(x, y) or board[x][y] ==6:
            return
        if board[x][y] != 0:
            continue
        board[x][y] = 7

n, m = map(int, input().split())
office_info = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * m for _ in range(n)]



mn = 0
coordinate = []
for i in range(n):
    for j in range(m):
        if office_info[i][j] != 0 and office_info[i][j] != 6:
            coordinate.append((i, j))
        if office_info[i][j] == 0:
            mn += 1

for tmp in range(1<<(2*len(coordinate))):
    for i in range(n):
        for j in range(m):
            board[i][j] = office_info[i][j]
    brute = tmp
    for i in range(len(coordinate)):
        dir = brute % 4
        brute //= 4
        x, y = coordinate[i][0], coordinate[i][1]
        if office_info[x][y] == 1:
            upd(x, y, dir)
        elif office_info[x][y] == 2:
            upd(x, y, dir)
            upd(x, y, dir + 2)
        elif office_info[x][y] == 3:
            upd(x, y, dir)
            upd(x, y, dir+1)
        elif office_info[x][y] == 4:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
        else:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
            upd(x, y, dir + 3)
        val = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    val += 1
        mn = min(mn, val)

print(mn)