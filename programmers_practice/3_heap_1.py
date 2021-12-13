import heapq

def solution(scoville, K):
    answer = 0
    print(scoville)
    heapq.heapify(scoville)
    print(scoville)
    # scoville.sort()
    # if scoville[-1] == 0:
    #     print(f'스코빌지수{K}를 만들 수 없음.')
    #     answer = -1
    # for i in range(len(scoville)-1):
    #     answer += 1
    #     scoville.insert(0, scoville.pop(0)+scoville.pop(0)*2)
    #     print(f'{answer}회차, 정렬 전{scoville}')
    #     scoville.sort()
    #     print(f'{answer}회차, 정렬 후{scoville}')
    #     if scoville[0] >= K:
    #         print('끝')
    #         break
    # if scoville[0] < K:
    #     print(f'스코빌지수{K}를 만들 수 없음.')
    #     answer = -1

    return answer


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 110
    print(solution(scoville, K))