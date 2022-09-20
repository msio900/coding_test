def solution(brown, yellow):
    answer = []
    stack = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            stack.append(i)
    for j, i in zip(range(len(stack)), reversed(range(len(stack)))):
        if 2*stack[i]+2*stack[j]+4 == brown:
            a, b = stack[i], stack[j]
            break
    answer = [a+2, b+2]

    return answer

# [1, 2]
# [1]
# [1, 2, 3, 4, 6, 8, 12, 24]

if __name__ == '__main__':
    brown, yellow = 10, 2
    print(solution(brown, yellow))
    brown, yellow = 8, 1
    print(solution(brown, yellow))
    brown, yellow = 24, 24
    print(solution(brown, yellow))
