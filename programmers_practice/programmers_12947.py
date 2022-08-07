def solution(x):
    nums = [int(i) for i in str(x)]
    if x % sum(nums)  == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    x = 10
    print(solution(x))
    x = 12
    print(solution(x))
    x = 11
    print(solution(x))
    x = 13
    print(solution(x))




