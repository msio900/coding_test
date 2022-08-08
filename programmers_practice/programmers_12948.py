def solution(phone_number):
    answer = '*'*(len(phone_number)-4)+phone_number[-4:]
    return answer

if __name__ == '__main__':
    phone_number = "01033334444"
    print(solution(phone_number))
    phone_number = "027778888"
    print(solution(phone_number))





