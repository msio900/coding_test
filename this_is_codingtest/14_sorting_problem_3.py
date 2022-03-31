def solution(N, stages):
    print(N, stages)
    stages.sort()
    answer = []
    for i in range(len(stages)):
        stage_user = []
        if stages[i] == stages[i+1]:
            stage_user.append(stages[i])
        answer.append(stage_user)
    print(answer)
    return answer


if __name__ == "__main__":
    N, stages = [5, [2, 1, 2, 6, 2, 4, 3, 3]]
    solution(N, stages)
