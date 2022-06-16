def solution(record):
    user_id = []
    nickname = []
    for i in record:
        if i.split()[0] == 'Enter':
            if i.split()[1] in user_id:
                nickname[user_id.index(i.split()[1])] = i.split()[2]
            else:
                user_id.append(i.split()[1])
                nickname.append(i.split()[2])
        # elif i.split()[0] == 'Leave':
        #     answer.append(f'{i.split()[2]}님이 나갔습니다.')
        if i.split()[0] == 'Change':
            nickname[user_id.index(i.split()[1])] = i.split()[2]
    # print(user_id)
    # print(nickname)
    answer = []
    for i in record:
        if i.split()[0] == 'Enter':
            answer.append(f'{nickname[user_id.index(i.split()[1])]}님이 들어왔습니다.')
        if i.split()[0] == 'Leave':
            answer.append(f'{nickname[user_id.index(i.split()[1])]}님이 나갔습니다.')