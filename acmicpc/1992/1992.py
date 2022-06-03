n = int(input())

tree = [list(map(int,(input()))) for _ in range(n)]
print(tree)
result = []

def quad_tree(x,y,n):
    global result
    color = tree[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != tree[i][j]: # 범위안에 한개라도 다른경우는 4분면으로 나눠서 다시 검색
                result.append("(") # 4분면으로 나눌때 괄호를 친다.
                quad_tree(x,y,n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(color) # 재귀로 안들어가고 for문이 전부 다 끝난 상태이기 때문에 범위안에 모든수가 같다고 볼 수 있다.

quad_tree(0,0,n)
print("".join(map(str,(result))))