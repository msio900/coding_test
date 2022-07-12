def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b, a + 1):
            answer += i
    elif a == b:
        answer = a
    else:
        for i in range(a, b+1):
            answer += i
    return answer

if __name__ == '__main__':
    a, b = 3,	5
    print(solution(a, b))
    a, b = 3,	3
    print(solution(a, b))
    a, b = 5,	3
    print(solution(a, b))


