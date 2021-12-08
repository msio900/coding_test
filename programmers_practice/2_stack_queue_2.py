def solution(priorities, location):
    answer = 0
    w_list = [i for i in range(len(priorities))]
    print(w_list)
    print(priorities)
    J = w_list[location]
    print('j는',J)
    point_idxs = []

    for i in range(len(priorities)):
        for j in range(i+1,len(priorities)):
            print('i : ',i,'j :',j)
            if priorities[i] < priorities[j]:
                point_idxs.append(i)
                break
    for point_idx in point_idxs:
        w_list.append(w_list[point_idx])
        print(w_list)
    for point_idx in point_idxs:
        w_list.pop(0)
        print(w_list)

    
    answer = w_list.index(J)+1
        

    return answer


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))