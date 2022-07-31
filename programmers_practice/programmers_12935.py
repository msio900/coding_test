def solution(arr):
    arr.remove(min(arr)) # 가장 작은 수 제거
    if arr: # 배열이 있을 경우
        return arr
    else: # 배열이 없을 경우
        return [-1]

if __name__ == '__main__':
    arr = [4,3,2,1]
    print(solution(arr))
    arr = [10]
    print(solution(arr))



