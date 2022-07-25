def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i ==0:
            answer += i
    return answer

if __name__ == '__main__':
    n = 12
    print(solution(n))
    n = 5
    print(solution(n))



