def solution(n, lost, reserve):
    students = [i for i in range(1, n+1) if i not in lost]

    for i in lost:
        if i in reserve:
            students.append(reserve.pop(reserve.index(i)))
        elif (i - 1) in reserve:
            students.append(reserve.pop(reserve.index(i - 1)))
        elif (i + 1) in reserve:
            students.append(reserve.pop(reserve.index(i + 1)))

    answer = len(students)
    return answer

if __name__ == '__main__':
    n, lost, reserve = 6, [2, 4, 6], [1, 2]
    print(solution(n, lost, reserve))
    n, lost, reserve = 5, [2, 4], [3]
    print(solution(n, lost, reserve))
    n, lost, reserve = 3, [3], [1]
    print(solution(n, lost, reserve))