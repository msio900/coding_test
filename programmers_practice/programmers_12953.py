from math import gcd

def LCM(x, y):
    result = (x*y)//gcd(x,y)
    return result

def solution(arr):
    answer = 0
    arr.sort(reverse=True)
    answer = LCM(arr[0], arr[1])
    for i in range(2, len(arr)):
        answer = LCM(answer, arr[i])

    return answer

if __name__ == '__main__':
    arr = [2,6,8,14]
    print(solution(arr))
    arr = [1,2,3]
    print(solution(arr))