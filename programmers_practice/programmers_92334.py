def solution(record):
    id_nickname = dict()
    for i in record:
        if i.split()[0] == 'Enter':
            id_nickname[i.split()[1]] = i.split()[2]
        if i.split()[0] == 'Change':
            id_nickname[i.split()[1]] = i.split()[2]

    answer = []
    for i in record:
        if i.split()[0] == 'Enter':
            answer.append(f'{id_nickname[i.split()[1]]}님이 들어왔습니다.')
        if i.split()[0] == 'Leave':
            answer.append(f'{id_nickname[i.split()[1]]}님이 나갔습니다.')
    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
