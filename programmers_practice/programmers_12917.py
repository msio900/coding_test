def solution(s):
    answer = ''.join(sorted(s, reverse=True))
    return answer

if __name__ == '__main__':
    s = "Zbcdefg"
    print(solution(s))


