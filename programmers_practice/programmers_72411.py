def solution(orders, course):
    answer = []
    print(orders)
    return answer

if __name__ == '__main__':
    orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
    print(solution(orders, course))
    orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
    print(solution(orders, course))
    orders, course = ["XYZ", "XWY", "WXA"], [2,3,4]
    print(solution(orders, course))
