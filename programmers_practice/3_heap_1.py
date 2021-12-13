def solution(scoville, K):
    answer = 0

    print(scoville.sorted())

    return answer


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 2
    print(solution(scoville, K))