def solution(s):
    answer = []
    s = s.replace('{', '')
    s_list = s.split('}')[:-2]
    s_list.sort(key=len)
    for i in s_list:
        temp = i.split(',')
        for j in temp:
            if j and j not in answer:
                answer.append(j)

    return list(map(int, answer))

if __name__ == '__main__':
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))
    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
    print(solution(s))
    s = "{{20,111},{111}}"
    print(solution(s))
    s = "{{123}}"
    print(solution(s))
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    print(solution(s))