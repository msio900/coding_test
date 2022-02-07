def solution(priorities, location):
    answer = 0
    w_list = list(range(len(priorities)))
    J = w_list[location]

    for i in range(len(priorities)):
        for j in range(i+1,len(priorities)):
            print('i : ',i,'j :',j)
            if priorities[i] < priorities[j]:
                print(priorities[i],":", priorities[j])

    answer = w_list.index(J)+1
        

    return answer


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))