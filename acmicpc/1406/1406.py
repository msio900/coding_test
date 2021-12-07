import sys

N_list = list(sys.stdin.readline().strip())

M = int(sys.stdin.readline())
cursor = len(N_list)

for _ in range(M):
    move = sys.stdin.readline().split()
    if move[0] == 'L':
        if cursor > 0:
            cursor -= 1

        else:
            pass

    if move[0] == 'D':
        if cursor < len(N_list):
            cursor += 1
        else:
            pass

    if move[0] == 'B':
        if cursor <= 0:
            pass
        else:
            del N_list[cursor-1]
            cursor -= 1

    if move[0] == 'P':
        N_list.insert(cursor, move[1])
        cursor += 1


print(N_list)