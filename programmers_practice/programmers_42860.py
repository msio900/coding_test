def solution(name):

    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    answer = 0
    alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    name_loc = [ord(i) - ord('A') for i in name]
    print(name_loc)
    return answer

if __name__ == '__main__':
    name = "JEROEN"
    print(solution(name))
    name = "JAN"
    print(solution(name))