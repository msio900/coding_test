def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer

if __name__ == '__main__':
    arr, divisor = [5, 9, 7, 10], 5
    print(solution(arr, divisor))
    arr, divisor = [2, 36, 1, 3], 1
    print(solution(arr, divisor))
    arr, divisor = [3, 2, 6], 10
    print(solution(arr, divisor))


