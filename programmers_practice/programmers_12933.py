def solution(n):
    n = [i for i in str(n)] # 정수형 자료 n을 리스트로 바꿈
    n.sort(reverse = True) # 내림차순 정렬
    return int(''.join(n)) # 리스트를 정수형 자료로 바꾼 후 반환

if __name__ == '__main__':
    n = 118372
    print(solution(n))



