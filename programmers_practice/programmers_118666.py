def solution(survey, choices):
    answer = ''
    character = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    character_score = [[0,0], [0,0], [0,0], [0,0]]
    survey_score = []
    for i in range(len(survey)):
        if choices[i] > 4:
            survey_score.append([survey[i][1], choices[i] - 4])
        else:
            survey_score.append([survey[i][0], 4 - choices[i]])
    for i in survey_score:
        if i[0] in character[0]:
            if i[0] == character[0][0]:
                character_score[0][0] += i[1]
            else:
                character_score[0][1] += i[1]
        elif i[0] in character[1]:
            if i[0] == character[1][0]:
                character_score[1][0] += i[1]
            else:
                character_score[1][1] += i[1]
        elif i[0] in character[2]:
            if i[0] == character[2][0]:
                character_score[2][0] += i[1]
            else:
                character_score[2][1] += i[1]
        else:
            if i[0] == character[3][0]:
                character_score[3][0] += i[1]
            else:
                character_score[3][1] += i[1]
    for i in range(4):
        if character_score[i][0] == character_score[i][1]:
            answer += sorted(character[i])[0]
        else:
            answer += character[i][character_score[i].index(max(character_score[i]))]



    return answer

if __name__ =='__main__':
    survey, choices = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
    print(solution(survey, choices))
    survey, choices = ["TR", "RT", "TR"], [7, 1, 3]
    print(solution(survey, choices))






