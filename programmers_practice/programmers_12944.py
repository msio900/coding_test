def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

if __name__ == '__main__':
    arr = [1,2,3,4]
    print(solution(arr))
    arr = [5,5]
    print(solution(arr))



