def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        if j == (len(prices)-1):
            answer.append(j-i)
    return answer


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]

    print(solution(prices))