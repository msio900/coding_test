def solution(s):
    s = s.replace('zero', '0')
    s = s.replace('one', '1')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')
    answer = s
    return answer

if __name__ == '__main__':
    s = "one4seveneight"
    print(solution(s))
    s = "23four5six7"
    print(solution(s))
    s = "2three45sixseven"
    print(solution(s))
    s = "123"
    print(solution(s))
