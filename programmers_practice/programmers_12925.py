def solution(n):
    s = '수박'
    answer = ''
    if n % 2 == 0:
        answer = s * (n // 2)
    else:
        answer = (s * (n // 2 + 1))[:-1]
    return answer

if __name__ == '__main__':
    n = 3
    print(solution(n))
    n = 4
    print(solution(n))



