from collections import defaultdict

def solution(n):
    d = defaultdict(int)
    d[1] = 1
    d[2] = 2
    for i in range(3, n+2):
        d[i] = (d[i-1]+d[i-2])%1234567

    return d[n]

if __name__ == '__main__':
    n = 4
    print(solution(n))
    n = 3
    print(solution(n))