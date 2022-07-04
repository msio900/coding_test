def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        num_arr = array[i - 1:j]
        num_arr.sort()
        answer.append(num_arr[k-1])
    return answer

if __name__ == '__main__':
    array, commands = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))
