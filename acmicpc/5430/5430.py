import sys

input = sys.stdin.readline

# R : 함수 R은 배열에 있는 수의 순서를 뒤집는 함수
# D : 첫 번째 수를 버리는 함수
# 열이 비어있는데 D를 사용한 경우에는 에러가 발생

# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    function = input().rstrip()
    n = int(input())
    array = input().rstrip()[1:-1].split(',')
    # print(function, n, array)
    if n != 0:
        for i in function:
            if i == 'R':
                array = array[::-1]
            if i == 'D':
                if array:
                    array.pop(0)
                else:
                    print('error')
                    break
        if len(array) != 0:
            print(f"[{','.join(array)}]")
    else:
        print('error')
    continue