def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i**2 == n: # i의 제곱이 n인지 확인
            return (i + 1)**2 # (x+1)의 제곱 반환
    else:
        return -1 # 없을경우 -1 반환

if __name__ == '__main__':
    n = 121
    print(solution(n))
    n = 3
    print(solution(n))



