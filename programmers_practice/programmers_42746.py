def solution(numbers):
    numbers.sort(key = lambda x : str(x) * 3, reverse = True)
    return str(int(''.join([str(i) for i in numbers])))

if __name__ =='__main__':
    numbers = [6, 10, 2]
    print(solution(numbers))
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))