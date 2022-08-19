from itertools import product

def solution(numbers, target):
    answer = 0
    num_list = []
    for i in numbers:
        num_list.append([i, -i])
    num_lists = list(product(*num_list))
    for i in num_lists:
        if sum(i) == target:
            answer += 1
    return answer

if __name__ =='__main__':
    numbers, target = [1, 1, 1, 1, 1], 3
    print(solution(numbers, target))
    numbers, target = [4, 1, 2, 1], 4
    print(solution(numbers, target))






