## 두 정수 사이의 합[↩](../programmers_practice)

> [두 정수 사이의 합](https://programmers.co.kr/learn/courses/30/lessons/12912)

## 🖋️문제

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

### 제한사항

- str은 길이 1 이상인 문자열입니다.

### 입출력 예

| s         | return    |
| --------- | --------- |
| "Zbcdefg" | "gfedcbZ" |

## 💡풀이

### 1차 시도

```python
def solution(s):
    answer = ''
    return answer
```

* 채점 결과

```python

```

### 성공😂
- a와 b 중 큰 수를 확인한 후 for 반복문을 이용하여 더해 줌.

