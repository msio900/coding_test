# for i, j in zip(range(10), reversed(range(10))):
#     print(i,j)



def solution(brown, yellow):
    answer = []
    stack = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            stack.append(i)
    print(stack)
    for j, i in zip(range(len(stack)), reversed(range(len(stack)))):
        if 2*stack[i]+2*stack[j]+4 == brown:
            a, b = stack[i], stack[j]
            break
    answer = [a+2, b+2]


    return answer



if __name__ == '__main__':
    brown = 24
    yellow = 24
    print(solution(brown, yellow))