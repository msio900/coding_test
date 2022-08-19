from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    dishes = []
    num_of_dishes = 0
    for i in orders:
        num_of_dishes = len(i)
        if num_of_dishes
        dishes += list(i)
    dishes = list(set(dishes))
    for i in range(2, )
    return answer

if __name__ == '__main__':
    orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
    print(solution(orders, course))
    orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
    print(solution(orders, course))
    orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]
    print(solution(orders, course))
