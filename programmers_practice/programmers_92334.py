from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))
    reported_num = {}
    reporting_num = {}
    for id in id_list:
        reported_num[id] = 0
        reporting_num[id] = 0
    for i in report:
        reported_num[i.split()[1]] += 1
    # print(reported_num.values())
    reported_id = []
    for id in reported_num:
        if reported_num[id] >= k:
            reported_id.append(id)

    for id in report:
        if id.split()[1] in reported_id:
            reporting_num[id.split()[0]] += 1
    # print(reporting_num)
    answer = list(reporting_num.values())



    return answer

if __name__ == '__main__':
    id_list, report, k, result = ["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2, [2, 1, 1, 0]
    print(solution(id_list, report, k))
    id_list, report, k, result = ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3, [0,0]
    print(solution(id_list, report, k))
