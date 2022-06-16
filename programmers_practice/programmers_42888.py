def solution(new_id):
    step1 = new_id.lower()

    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    step2 = ''
    for i in step1:
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.':
            step2 += i
    print('step2', step2)
    step3 = ''
    dot = []
    for i in step2:
        # print(i)
        if i == '.':
            dot.append(i)
        if not dot and i != '.':
            step3 += i
        if dot and i != '.':
            step3 += '.'
            dot = []
            step3 += i
    print('step3', step3)
    step4 = step3.strip('.')
    print('step4', step4)
    if not step4:
        step5 = 'a'
    else:
        step5 = step4
    print('step5', step5)
    if len(step5) >= 16:
        step6 = step5[:15]
    else:
        step6 = step5
    print('step6', step6)
    step7 = step6
    if len(step7) <= 2:
        while len(step7) != 3:
            step7 += step7[-1]
    print('step7', step7)

    answer = step7.strip('.')
    return answer