def solution(name):
    answer = 0
    alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    # for i in name:
    #     answer += 1
    #     if i =='A':
    #         pass
    #     elif temp < alpha.index(i):
    #         print('▼', alpha[temp:alpha.index(i)], len(alpha[temp:alpha.index(i)]))
    #         print('▲', alpha[:temp]+alpha[alpha.index(i):], len(alpha[:temp]+alpha[alpha.index(i):]))
    #         print(min([len(alpha[temp:alpha.index(i)]), len(alpha[:temp] + alpha[alpha.index(i):])]))
    #         answer += min([len(alpha[temp:alpha.index(i)]), len(alpha[:temp]+alpha[alpha.index(i):])])
    #     elif temp > alpha.index(i):
    #         print('▼', alpha[alpha.index(i):temp], len(alpha[alpha.index(i):temp]))
    #         print('▲', alpha[:alpha.index(i)] + alpha[temp:], len(alpha[:alpha.index(i)] + alpha[temp:]))
    #         print(min([len(alpha[alpha.index(i):temp]), len(alpha[:alpha.index(i)] + alpha[temp:])]))
    #         answer += min([len(alpha[alpha.index(i):temp]), len(alpha[:alpha.index(i)] + alpha[temp:])])
    #     temp = alpha.index(i)
    for i in name:
        answer += min([len(alpha[alpha.index(i):]), len(alpha[:alpha.index(i)])])
        # if alpha.index(i) > 12:
        #     print(alpha[alpha.index(i):], len(alpha[alpha.index(i):]))
        #     answer += len(alpha[alpha.index(i):])
        # elif alpha.index(i) < 12:
        #     print(alpha[:alpha.index(i)],len(alpha[:alpha.index(i)]))
        #     answer += len(alpha[:alpha.index(i)])
        # elif i == 'N':
        #     answer += 11
    answer += len(name) - 1

    return answer

if __name__ == '__main__':
    name = "JEROEN"
    print(solution(name))
    name = "JAN"
    print(solution(name))