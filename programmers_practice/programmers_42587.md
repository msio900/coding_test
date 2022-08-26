## 프린터[↩](../programmers_practice)

[프린터](https://programmers.co.kr/learn/courses/30/lessons/42587)

## 🖋️문제

일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

```
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
```

예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.

- 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
- location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

### 입출력 예

| priorities         | location | return |
| ------------------ | -------- | ------ |
| [2, 1, 3, 2]       | 2        | 1      |
| [1, 1, 9, 1, 1, 1] | 0        | 5      |

### 입출력 예 설명

**예제 #1**

문제에 나온 예와 같습니다.

**예제 #2**

6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.

## 💡풀이

### 1차 시도

```python
from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    positions = deque(range(len(priorities)))
    answer = 0
    while priorities[0] != max(priorities):
        priorities.append(priorities.popleft())
        positions.append(positions.popleft())
            
    return positions.index(location) + 1
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	실패 (0.01ms, 10.2MB)
테스트 3 〉	실패 (0.02ms, 10.2MB)
테스트 4 〉	실패 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	실패 (0.01ms, 10.2MB)
테스트 7 〉	실패 (0.01ms, 10.2MB)
테스트 8 〉	실패 (0.03ms, 10.3MB)
테스트 9 〉	실패 (0.01ms, 10.2MB)
테스트 10 〉	실패 (0.01ms, 10.1MB)
테스트 11 〉	실패 (0.01ms, 10.4MB)
테스트 12 〉	실패 (0.01ms, 10.1MB)
테스트 13 〉	실패 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	실패 (0.01ms, 10.3MB)
테스트 17 〉	실패 (0.06ms, 10.2MB)
테스트 18 〉	실패 (0.01ms, 10.1MB)
테스트 19 〉	실패 (0.08ms, 10.3MB)
테스트 20 〉	실패 (0.02ms, 10.1MB)
채점 결과
정확성: 20.0
합계: 20.0 / 100.0
```

### 실패😂

* while 반복문을 우선순위가 가장 큰 값이 첫번째 순서에 올 때까지 반복하여 출력 순서에 맞는 배열 도출

  ```python
  while priorities[0] != max(priorities):
      priorities.append(priorities.popleft())
      positions.append(positions.popleft())
  ```

  

### 2차 시도

```python
from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    positions = deque(range(len(priorities)))
    answer = 0
    while True:
        max_priority = max(priorities)
        if  priorities[0] == max_priority:
            answer += 1
            if positions[0] == location:
                break
            priorities.popleft()
            positions.popleft()
        else:
            priorities.append(priorities.popleft())
            positions.append(positions.popleft())
            
    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.4MB)
테스트 2 〉	통과 (0.66ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.08ms, 10.1MB)
테스트 7 〉	통과 (0.08ms, 10.2MB)
테스트 8 〉	통과 (0.43ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.09ms, 10.2MB)
테스트 11 〉	통과 (0.32ms, 10.1MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.53ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.06ms, 10.4MB)
테스트 17 〉	통과 (0.94ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.35ms, 10.1MB)
테스트 20 〉	통과 (0.10ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

### 성공😊

* 문제의 컨셉대로 순서를 정함.

* 배열 1번째 출력물의 우선순위가 가장 큰 지 확인

  * 가장 크다면 출력하도록 `popleft()`
  * 크지 않다면 `popleft()`한 값을 `append()`

* 출력할때 마다 `answer += 1`을 하여 `location` 값까지의 출력 순서를 구함

* 배열 1번째 출력물 남아있는 배열에서 우선순위가 가장 크고 배열이  `location`과 같다면 반복문 탈출

  ```python
  if positions[0] == location:
      break
  ```

