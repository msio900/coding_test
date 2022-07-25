def solution(s):
    ans_word = []
    words = s.split(' ') # 문자열을 공백을 기준으로 단어를 나누어 리스트로 만들어 줌.
    for i in words: # 단어 하나씩 반복문으로 꺼내줌.
        word = ''
        for j in range(len(i)): # 단어 안에 문자 확인
            if j % 2 == 0: # 짝수 번째일 경우 대문자로 변환
                word += i[j].upper()
            else: # 홀수 번째 일 경우 소문자로 변환
                word += i[j].lower()
        ans_word.append(word)
    return ' '.join(ans_word)

if __name__ == '__main__':
    s = "try hello world"
    print(solution(s))



