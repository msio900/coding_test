def solution(answers):
    answer = []
    A = []
    B = []
    C = []
    # 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    for i in range(len(answers)):
        A.append(i+1 - 5*(i//5))
    # 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    for i in range(len(answers)):
        if i//2 == 0:
            print(i)
        A.append(i+1 - 5*(i//5))
    # 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    return answer



if __name__ == '__main__':
    answers = [1,2,3,4,5]
    print(solution(answers))