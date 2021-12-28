# 탐욕법(Greedy)3 : 큰 수 만들기[↩](../programmers_practice)

[탐욕법(Greedy)3 : 큰 수 만들기](https://programmers.co.kr/learn/courses/30/lessons/42883)

## 🖋️문제

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

### 제한사항

- number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
- k는 1 이상 `number의 자릿수` 미만인 자연수입니다.

### 입출력 예

| number       | k    | return   |
| ------------ | ---- | -------- |
| "1924"       | 2    | "94"     |
| "1231234"    | 3    | "3234"   |
| "4177252841" | 4    | "775841" |

## 💡풀이
### 1차시도
```python
from itertools import combinations

def solution(number, k):
    answer = ''
    number_list = list(map(str, number))
    answer_list = []
    for i in combinations(number_list, len(number_list)-k):
        answer_list.append(''.join(i))

    answer_list.sort(reverse=True)
    answer = answer_list[0]

    return answer
```

* 채점 결과

```python
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (1087.90ms, 188MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
채점 결과
정확성: 33.3
합계: 33.3 / 100.0
```

### 실패😂
* `itertools`라이브러리를 사용하여, 조합함.
* 시간 초과...
### 2차 시도
```python
def solution(number, k):
    answer = []  # Stack
    cnt = 0
    for num in number:
        cnt+= 1
        if not answer:
            print(f'{cnt}회, num : {num}이 answer에 없을 경우')
            answer.append(num)
            print('answer', answer)
            continue
        if k > 0:
            print(f'{cnt}회, k : {k}이 0보다 큰 경우')
            while answer[-1] < num:
                print(f'answer[-1] : {answer[-1]}이 num : {num}보다 작을때까지 반복')
                answer.pop()
                print('answer', answer)
                k -= 1
                if not answer or k <= 0:
                    print(f'answer : {answer}, k : {k}')
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

if __name__ == '__main__':
    number = "4177252841"
    k = 4
    print(solution(number, k))
```
### 성공😀
* 약간의 구글링...역시 그리디를 구현해내는 부분에 있어서 많이 약하다...
* 스택에 한 숫자씩 채워넣기!


### 🤝다른 풀이

* 프로그래머스 풀이

```python
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
```

* 찬구

```java

```

* 준오

```python

```

* 경현

```java

```

* 숙영

```python

```

