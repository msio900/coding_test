## 타겟 넘버 [↩](../programmers_practice)

> [타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)

## 🖋️문제

n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

```
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

### 입출력 예

| numbers         | target | return |
| --------------- | ------ | ------ |
| [1, 1, 1, 1, 1] | 3      | 5      |
| [4, 1, 2, 1]    | 4      | 2      |

### 입출력 예 설명

**입출력 예 #1**

문제 예시와 같습니다.

**입출력 예 #2**

```
+4+1-2+1 = 4
+4-1+2-1 = 4
```

- 총 2가지 방법이 있으므로, 2를 return 합니다.

## 💡풀이

### 1차 시도

```python
from itertools import product

def solution(numbers, target):
    answer = 0
    num_list = []
    for i in numbers:
        num_list.append([i, -i])
    num_lists = list(product(*num_list))
    for i in num_lists:
        if sum(i) == target:
            answer += 1 
    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (596.29ms, 234MB)
테스트 2 〉	통과 (570.73ms, 234MB)
테스트 3 〉	통과 (0.34ms, 10.3MB)
테스트 4 〉	통과 (1.51ms, 10.5MB)
테스트 5 〉	통과 (14.59ms, 15.4MB)
테스트 6 〉	통과 (0.74ms, 10.2MB)
테스트 7 〉	통과 (0.36ms, 10.4MB)
테스트 8 〉	통과 (3.46ms, 11MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

### 성공😊
- python 라이브리러 `itertools`의 `product()`기능을 활용하여 해결
- 리스트 `numbers`안에 들어있는 수들의 양수, 음수의 리스트를 만든 후 이를 `product()`로 조합 추출하여 리스트에 담음
- 이후 `sum()`조합된 리스트가 `target`수와 같은지 확인

