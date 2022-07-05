def solution(answers):
    one_supo = [1, 2, 3, 4, 5]*(len(answers)//5+1)
    two_supo = [2, 1, 2, 3, 2, 4, 2, 5]*(len(answers)//8+1)
    three_supo = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answers)//10+1)
    each_cnt = [0,0,0]
    print(one_supo, two_supo, three_supo)
    for i in range(len(answers)):
        if one_supo[i] == answers[i]:
            each_cnt[0] +=1
        if two_supo[i] == answers[i]:
            each_cnt[1] +=1
        if three_supo[i] == answers[i]:
            each_cnt[2] +=1
    print(each_cnt)

    answer = []
    for k, v in enumerate(each_cnt):
        if v == max(each_cnt):
            answer.append(k + 1)
    return answer

if __name__ == '__main__':
    answers = [1,2,3,4,5]
    print(solution(answers))
    answers = [1,3,2,4,2]
    print(solution(answers))