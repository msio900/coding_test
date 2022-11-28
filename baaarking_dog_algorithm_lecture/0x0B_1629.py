import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())


# pow 모듈 활용
# print(pow(a, b, c))
def solution(a : int, b : int, c : int) -> int:
    if b == 1:
        return a % c
    val = solution(a, b//2, c)
    val = val * val % c
    if b % 2 == 0:
        return val
    return val * a % c

print(solution(a, b, c))