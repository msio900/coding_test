from itertools import product

def solution(expression):
    answer = 0
    nums = []
    ops = []
    num = ''
    for i in expression:
        if i.isnumeric():
            num += i
        else:
            nums.append(int(num))
            ops.append(i)
            num = ''
    nums.append(int(num))

    print(nums, ops)

    return answer

if __name__ == '__main__':
    expression = "100-200*300-500+20"
    print(solution(expression))
    expression = "50*6-3*2"
    print(solution(expression))



