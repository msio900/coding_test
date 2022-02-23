# def solution(prices):
#     answer = []
#     for i in range(0, len(prices)):
#         for j in range(i+1, len(prices)):
#             if j == (len(prices)-1) :
#                 answer.append(j-i)
#             elif prices[i] >prices[j]:
#                 answer.append(j-i)
#                 break
#     answer.append(0)
#
#     return answer
#
#
# if __name__ == '__main__':
#     prices = [1, 2, 3, 2, 3]
#
#     print(solution(prices))


def solution(prices):

    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        if len(stack) != 0:
            for j in range(len(stack)):
                if prices[i] < prices[stack[-1]]:
                    tp = stack.pop()
                    answer[tp] = i - tp
                else:
                    break
        stack.append(i)

    for k in stack:
        answer[k] = len(answer) - k - 1

    return answer


if __name__ == '__main__':
    prices = [3, 2, 4, 5, 1]

    print(solution(prices))