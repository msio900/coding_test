def solution(number, k):
    answer = []  # Stack
    cnt = 0
    for num in number:
        cnt+= 1
        if not answer:
            print(f'{cnt}회, num : {num}이 answer에 없을 경우')
            answer.append(num)
            print('answer', answer)
            continue
        if k > 0:
            print(f'{cnt}회, k : {k}이 0보다 큰 경우')
            while answer[-1] < num:
                print(f'answer[-1] : {answer[-1]}이 num : {num}보다 작을때까지 반복')
                answer.pop()
                print('answer', answer)
                k -= 1
                if not answer or k <= 0:
                    print(f'answer : {answer}, k : {k}')
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

if __name__ == '__main__':
    number = "4177252841"
    k = 4
    print(solution(number, k))