def solution(name):
    answer = 0
    alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    for i in range(len(name)):
        answer += min([len(alpha[alpha.index(name[i]):]), len(alpha[:alpha.index(name[i])])])

    return answer


if __name__ == '__main__':
    name = "JEROEN"
    print(solution(name))
    name = "JAN"
    print(solution(name))