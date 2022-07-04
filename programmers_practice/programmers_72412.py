from itertools import product

def solution(info, query):
    data = dict()

    lang = ['cpp', 'java', 'python', '-']
    group = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']

    infos = list(product(lang, group, career, food))

    for i in infos:
        data[i] = []


    for i in infos:
        data[i] = []

    for i in info:
        i = i.split()
        for i_lang in [i[0], '-']:
            for i_group in [i[1], '-']:
                for i_career in [i[2], '-']:
                    for i_food in [i[3], '-']:
                        data[(i_lang, i_group, i_career, i_food)].append(int(i[4]))
    for i in data:
        data[i].sort()

    answer = []

    for q in query:
        q = q.replace('and', '').split()

        info_q = data[(q[0], q[1], q[2], q[3])]
        score = int(q[4])
        l = 0
        r = len(info_q)
        mid = 0

        while l < r:
            mid = (r + l) // 2
            if info_q[mid] >= score:
                r = mid
            else:
                l = mid + 1
        answer.append(len(info_q) - l)

    # 민성 1차 시도
    # for i in query:
    #     i = i.replace('and','')
    #     # print(i.split()[0], i.split()[1], i.split()[2], i.split()[3], i.split()[4])
    #     lng, part, exp, soul_food, score = i.split()[0], i.split()[1], i.split()[2], i.split()[3], i.split()[4]
    #     cnt = 0
    #     for j in info:
    #         print(f'lng: {lng} part: {part} exp: {exp} soul_food: {soul_food} score: {score}')
    #         print(j.split()[0], j.split()[1], j.split()[2], j.split()[3], j.split()[4])
    #         if (lng == j.split()[0] or lng == '-') and (part == j.split()[1] or part == '-') and (exp == j.split()[2] or exp == '-') and (soul_food == j.split()[3] or soul_food == '-') and (int(score) <= int(j.split()[4]) or score == '-'):
    #             cnt += 1
    #     answer.append(cnt)

    return answer

if __name__ == '__main__':
    info, query = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))
