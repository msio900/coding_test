from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer

if __name__ == '__main__':
    n, m = 3, 12
    print(solution(n, m))
    n, m = 2, 5
    print(solution(n, m))



