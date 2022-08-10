def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

if __name__ == '__main__':
    x, n = 2, 5
    print(solution(x, n))
    x, n = 4, 3
    print(solution(x, n))
    x, n = -4, 2
    print(solution(x, n))





