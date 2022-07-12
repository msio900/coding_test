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
    return answer
```

* 채점 결과

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
