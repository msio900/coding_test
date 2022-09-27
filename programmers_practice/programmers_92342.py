def solution(n, info):
    answer = []
    return answer

if __name__ == "__main__":
    inputs = [
        [5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]],
        [1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        [9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]],
        [10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]]
    ]
    for i in range(len(inputs)):
        print(f'{i+1}st test case', solution(inputs[i][0],inputs[i][1]))