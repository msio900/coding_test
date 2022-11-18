import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # 장소의 크기 N*M
matrix = [[0] * m for _ in range(n)] # 방문 여부를 파악하기 위한 행렬

x, y, direction = map(int, input().split()) # 현재 위치 (x, y), 바라보는 방향 direction
matrix[x][y] = 1 # 현재 위치에 방문 처리

mapping = [list(map(int, input().split())) for _ in range(n)] # 빈칸(0)과 벽(1)의 여부를 담은 행렬

# 북 - 동 - 남 - 서 를 index로 표현
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 도는 경우를 함수로 규정
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

answer = 1 # 현재 위치에서 출발하기 때문에 1부터 시작
turn_time = 0 # 회전한 횟수

while True:
    turn_left() # 왼쪽 방향으로 회전
    nx, ny = x + dx[direction], y + dy[direction] # 회전한 좌표

    if matrix[nx][ny] == 0 and mapping[nx][ny] == 0: # 회전한 좌표가 방문하지 않았고 벽이 아닌 경우
        matrix[nx][ny] = 1 # 방문 여부 행렬에 방문 처리
        x, y = nx, ny # 해당 위치로 이동
        answer += 1 # 청소하는 칸의 개수에 1을 더함
        turn_time = 0 # 회전한 횟수 초기화
        continue
    else:
        turn_time += 1 # 추가로 회전

    if turn_time == 4: # 360도 회전한 경우
        nx, ny = x - dx[direction], y - dy[direction] # 다시 돌아가기
        if mapping[nx][ny] == 0: # 돌아간 위치가 벽이 아니면
            x, y = nx, ny # 해당 위치로 이동
        else: # 360도로 회전했는데 돌아간 위치가 모두 벽이라면 탈출
            break
        turn_time = 0 # 회전한 횟수 초기화
print(answer)