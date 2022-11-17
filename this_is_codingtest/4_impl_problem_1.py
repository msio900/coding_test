import sys

input = sys.stdin.readline

pos = input().rstrip()

x, y = ord(pos[0])- ord('a'), int(pos[1])-1

# 왕실의 나이트가 갈 수 있는 방법
cases = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]

answer = []
for i in cases:
    print(f'{x} + {i[0]}: {x + i[0]}, {y} + {i[1]} : {y + i[1]}')
    if 7 >= x + i[0] >= 0 and 7 >= y + i[1] >= 0:
        answer.append([x + i[0], y + i[1]])
print(len(answer))