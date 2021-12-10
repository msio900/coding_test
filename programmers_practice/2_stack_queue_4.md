# 스택/큐4 : 주식 가격[↩](../programmers_practice)

[스택/큐4 : 주식 가격](https://programmers.co.kr/learn/courses/30/lessons/42584)

## 🖋️문제

 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

### 제한사항

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

### 입출력 예

| prices          | return          |
| --------------- | --------------- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

### 입출력 설명

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.



## 💡풀이

### 1차 시도

```python
def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        if j == (len(prices)-1):
            answer.append(j-i)
    return answer


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]

    print(solution(prices))
```

* 채점 결과

```python
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.57ms, 10.3MB)
테스트 4 〉	통과 (0.71ms, 10.3MB)
테스트 5 〉	실패 (0.85ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.37ms, 10.3MB)
테스트 8 〉	실패 (0.89ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.84ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (108.22ms, 18.8MB)
테스트 2 〉	실패 (82.69ms, 17.6MB)
테스트 3 〉	통과 (117.13ms, 19.6MB)
테스트 4 〉	통과 (93.83ms, 18.3MB)
테스트 5 〉	실패 (63.96ms, 17.1MB)
채점 결과
정확성: 53.3
효율성: 13.3
합계: 66.7 / 100.0
```

### 실패😂

* 테스트 케이스에서는 통과되나, 제출 시 미통과

### 2차 시도😂

```python
def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if j == (len(prices)-1) :
                answer.append(j-i)
            elif prices[i] >prices[j]:
                answer.append(j-i)
                break
    answer.append(0)
            
    return answer


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]

    print(solution(prices))
```

* 채점 결과

```python
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.4MB)
테스트 3 〉	통과 (0.93ms, 10.3MB)
테스트 4 〉	통과 (0.93ms, 10.4MB)
테스트 5 〉	통과 (1.29ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.53ms, 10.3MB)
테스트 8 〉	통과 (0.62ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (1.27ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (184.48ms, 18.9MB)
테스트 2 〉	통과 (144.18ms, 17.6MB)
테스트 3 〉	통과 (233.12ms, 19.5MB)
테스트 4 〉	통과 (173.58ms, 18.3MB)
테스트 5 〉	통과 (99.50ms, 17.1MB)
채점 결과
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
```

### 성공😊

* if-elif문을 활용하여 효율성 개선

### 🤝다른 풀이

* 찬구

```java

```
