import sys

input = sys.stdin.readline

n, m = map(int, input().split())
office_info = [list(map(int, input().split())) for _ in range(n)]


# 1. CCTV가 있는 좌표와 벽이 있는 좌표를 찾는다.

coordinate = []
for i in range(n):
    for j in range(m):
        if office_info[i][j]:
            coordinate.append([i, j])
# 2. 각 CCTV가 감시하는 방향의 경우의 수마다 사각지대의 개수를 구한다.

# 3. 사각지대 개수의 최소값을 출력한다.

