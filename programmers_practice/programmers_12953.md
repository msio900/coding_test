# N개의 최소공배수[↩](../programmers_practice)

[N개의 최소공배수](https://programmers.co.kr/learn/courses/30/lessons/12953)

## 🖋️문제

두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

### 제한사항

- arr은 길이 1이상, 15이하인 배열입니다.
- arr의 원소는 100 이하인 자연수입니다.

### 입출력 예

| arr        | result |
| ---------- | ------ |
| [2,6,8,14] | 168    |
| [1,2,3]    | 6      |

## 💡풀이

```python
from math import gcd

def LCM(x, y): # 최소공배수를 구하는 함수 구현
    result = (x*y)//gcd(x,y) # 두 값을 곱한 값을 최대공약수로 나눔
    return result

def solution(arr):
    answer = 0
    # arr.sort(reverse=True)
    answer = LCM(arr[0], arr[1])
    for i in range(2, len(arr)):
        answer = LCM(answer, arr[i])

    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

- 상위 두 값의 `LCM`를 구함.
- 앞서 구한 `LCM`과 리스트 상의 다음 값의 LCM을 구하는 것을 반복함.
- 최종적으로 리스트 모든 수의 `LCM` 도출

### 성공😊

### 🤝다른 풀이

