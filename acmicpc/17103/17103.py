import sys


def prime_list(n):      # 에라토스테네스의 체 함수
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

T = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(T)]
N_prime_list = prime_list(max(nums))
# print(N_prime_list)
for num in nums:
    answer = 0
    for i, j in zip(reversed(range(1, num)), range(1, num)):
        if i > num//2 - 1:
            # print(i, j)
            if (i in N_prime_list) and (j in N_prime_list):
                answer += 1

    print(answer)

