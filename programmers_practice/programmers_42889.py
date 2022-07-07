def solution(N, stages):
    stages_fail = [0]*N
    # print(stages_fail)
    stages.sort()
    # print(stages)
    for k, v in enumerate(stages_fail):
        print('enumerate',k, v)
        place = 0
        while stages[place] - 1 != k:
            print(k, stages[place])
            place +=1
    answer = []
    return answer

if __name__ == '__main__':
    N, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(N, stages))
    N, stages = 4, [4,4,4,4,4]
    print(solution(N, stages))
