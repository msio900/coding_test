from itertools import combinations

def solution(relation):
    x, y = len(relation[0]), len(relation)
    col = list(range(x))
    cases = []
    uniques = []
    for i in range(1, x + 1):
        case = list(combinations(col, i))
        cases += case
    for case in cases:
        # print(case)
        keys = []
        for j in range(y):
            key = ''
            for i in case:
                key += relation[j][i]
            keys.append(key)
        if len(keys) == len(set(keys)):
            for x in uniques:
                if set(x).issubset(set(case)):
                    break
            else:
                uniques.append(list(case))

    return len(uniques)


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(f'답은 {solution(relation)}')