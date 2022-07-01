def solution(board, moves):
    n = len(board)
    for i in board:
        print(i)
    doll_arr = []
    ans_arr = []
    for i in moves:
        depth = 0
        while True:
            if board[len(board)-1][i - 1] == 0:
                break
            doll = board[depth][i - 1]
            if doll != 0:
                doll_arr.append(board[depth][i - 1])
                board[depth][i - 1] = 0
                break
            if len(doll_arr) > 2:
                print(doll_arr)
                while doll_arr[-1] != doll_arr[-2]:
                    print(doll_arr)
                    ans_arr.append(doll_arr.pop())
                    ans_arr.append(doll_arr.pop())
            depth +=1
    print('변화 후')
    for i in board:
        print(i)
    print(ans_arr)
    answer = len(ans_arr)
    return answer

if __name__ == '__main__':
    board, moves = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]
    print(solution(board, moves))
