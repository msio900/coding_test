from itertools import combinations


def solution(relation):
    x, y = len(relation[0]), len(relation)  # x :num of rows y : num of columns
    col = list(range(x))  # for presenting columns cases
    cases = []
    uniques = []
    # candidate key's combination list
    for i in range(1, x + 1):
        case = list(combinations(col, i))  #
        cases += case

    for case in cases:  # 'case': each candidate key column
        keys = []
        for j in range(y):
            key = ''
            for i in case:
                key += relation[j][i]
            keys.append(key)
        if len(keys) == len(set(keys)):  # varify uniqueness
            for x in uniques:
                if set(x).issubset(set(case)):  # varify minimality
                    break
            else:
                uniques.append(list(case))

    return len(uniques)


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(f'답은 {solution(relation)}')