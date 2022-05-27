# n : 양의 정수
# k : 바꿀 진수
# 아래 조건에 맞는 소수가 몇개인지?
# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.



def solution(n, k):
    # n을 k 진수로 바꾸기
    k_list = []
    while n != 0:
        k_list.append(n % k)
        n //= k
        print(k_list, n)
    answer = -1

    return answer

if __name__ == "__main__":
    n, k = 437674, 3
    print('1st Test Case', solution(n, k))
    n, k = 110011, 10
    print('2nd Test Case', solution(n, k))