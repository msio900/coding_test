def solution(s, n):
    alpha_low = [chr(i) for i in range(ord('a'), ord('z')+1)]*2
    alpha_upp = [chr(i) for i in range(ord('A'), ord('Z')+1)]*2
    answer = ''
    for i in s:
        if i.islower():
            answer += alpha_low[(ord(i)-ord('a'))+n]
        elif i.isupper():
            answer += alpha_upp[(ord(i)-ord('A'))+n]
        else:
            answer += i
    return answer

if __name__ == '__main__':
    s, n = "AB", 1
    print(solution(s, n))
    s, n  = "z", 1
    print(solution(s, n))
    s, n = "a B z", 4
    print(solution(s, n))




