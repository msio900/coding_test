def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],
              [4,5,6],
              [7,8,9],
              ['*', 0, '#']]
    pre_L = 0
    pre_R = 0
    print(keypad[0].index(1))
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            pre_L = i
        if i in [3, 6, 9]:
            answer += 'R'
            pre_R = i
        # if i in [2, 5, 8, 0]:



    return answer

if __name__ == '__main__':
    numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"
    print(solution(numbers, hand))
    numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"
    print(solution(numbers, hand))
    numbers, hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"
    print(solution(numbers, hand))