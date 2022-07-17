def solution(s):
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False

if __name__ == '__main__':
    s = "a234"
    print(solution(s))
    s = "1234"
    print(solution(s))



