def solution(numbers):
    numbers.sort(key = lambda x : str(x) * 3, reverse = True)
    return str(int("".join(list(map(str, numbers)))))


if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))