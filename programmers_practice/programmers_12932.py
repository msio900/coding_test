def solution(n):
    answer = []
    for i in reversed(str(n)): # 자연수 n을 문자열로 변환한 뒤 뒤집어서 반복
        answer.append(int(i)) # 반복문에서 반환되는 문자를 정수로 변환뒤 리스트에 입력
    return answer

if __name__ == '__main__':
    n = 12345
    print(solution(n))



