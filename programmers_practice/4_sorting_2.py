def solution(jobs):
    answer = 0
    for i in range(0,len(jobs)):
        print(jobs[i][1]-jobs[i+1][0]+jobs[i+1][1])


    return answer


if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    print(solution(jobs))