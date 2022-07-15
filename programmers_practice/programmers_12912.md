## 두 정수 사이의 합[↩](../programmers_practice)

> [두 정수 사이의 합](https://programmers.co.kr/learn/courses/30/lessons/12912)

## 🖋️문제

두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

### 제한사항

- a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
- a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
- a와 b의 대소관계는 정해져있지 않습니다.

### 입출력 예

| a    | b    | return |
| ---- | ---- | ------ |
| 3    | 5    | 12     |
| 3    | 3    | 3      |
| 5    | 3    | 12     |

## 💡풀이

### 1차 시도

```python
def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b, a + 1):
            answer += i
    elif a == b:
        answer = a
    else:
        for i in range(a, b+1):
            answer += i
    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (853.01ms, 10.3MB)
테스트 5 〉	통과 (594.13ms, 10.2MB)
테스트 6 〉	통과 (493.47ms, 10.2MB)
테스트 7 〉	통과 (260.51ms, 10.2MB)
테스트 8 〉	통과 (388.14ms, 10.1MB)
테스트 9 〉	통과 (303.98ms, 10.2MB)
테스트 10 〉	통과 (66.68ms, 10.3MB)
테스트 11 〉	통과 (0.22ms, 10.1MB)
테스트 12 〉	통과 (0.64ms, 10.2MB)
테스트 13 〉	통과 (0.26ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.1MB)
테스트 16 〉	통과 (0.13ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

### 성공😂
- a와 b 중 큰 수를 확인한 후 for 반복문을 이용하여 더해 줌.

## 다른 풀이

> 정화님 풀이
```python
def sum_gauss(n):
    return int(n*(n+1)/2)

def solution(a, b):
    answer = 0
    
    if a >= b:
        answer = sum_gauss(a) - sum_gauss(b-1)
    else:
        answer = sum_gauss(b) - sum_gauss(a-1)
        
    return answer
```
