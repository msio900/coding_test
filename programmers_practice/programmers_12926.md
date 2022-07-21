## 시저 암호[↩](../programmers_practice)

> [시저 암호](https://programmers.co.kr/learn/courses/30/lessons/12926)

## 🖋️문제

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

### 제한사항

- 공백은 아무리 밀어도 공백입니다.
- s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
- s의 길이는 8000이하입니다.
- n은 1 이상, 25이하인 자연수입니다.

### 입출력 예

| s       | n    | result  |
| ------- | ---- | ------- |
| "AB"    | 1    | "BC"    |
| "z"     | 1    | "a"     |
| "a B z" | 4    | "e F d" |

## 💡풀이

### 1차 시도

```python
def solution(s, n):
    alpha_low = [chr(i) for i in range(ord('a'), ord('z')+1)]*2
    alpha_upp = [chr(i) for i in range(ord('A'), ord('Z')+1)]*2
    answer = ''
    for i in s:
        if i.islower():
            answer += alpha_low[(ord(i)-ord('a'))+n]
        elif i.isupper():
            answer += alpha_upp[(ord(i)-ord('A'))+n]
        else:
            answer += i
    return answer
```

* 채점 결과

```python
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (1.47ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

### 성공😊
- 암호를 결정하는 숫자인 `n`이 1이상 25 이하인 수이므로 알파벳 대문자 소문자의 배열을 1번 반복한 배열을 만들어줌
- 문자열 `s`를 for반복문으로 추출하여 해당 문자가 대소문자 여부와 그 외의 다른 글자인지 검증해줌.

