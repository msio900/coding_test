def solution(num):
    answer = 0
    if num == 1: # 주어진 수가 이미 1일 경우
        return 0
    else:
        while num != 1: # 주어진 수가 1이 될 때까지
            if num % 2 == 0:
                answer += 1
                num //= 2
            else:
                answer += 1
                num *= 3
                num += 1
        if answer > 500: # 횟수가 500 이상일 경우
            return -1
        return answer

if __name__ == '__main__':
    n = 6
    print(solution(n))
    n = 16
    print(solution(n))
    n = 626331
    print(solution(n))



