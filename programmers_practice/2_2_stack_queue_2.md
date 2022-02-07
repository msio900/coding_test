# 스택/큐2 : 프린터[↩](../programmers_practice)

[스택/큐2 : 프린터](https://programmers.co.kr/learn/courses/30/lessons/42587)

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

* 예제 #1
  
  문제에 나온 예와 같습니다.
  
* 예제 #2

  6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.

## 💡풀이

* 풀이 1

```python
def solution(priorities, location):
    answer = 0
    w_list = [i for i in range(len(priorities))]
    print(w_list)
    print(priorities)
    J = w_list[location]
    print('j는',J)
    point_idxs = []

    for i in range(len(priorities)):
        for j in range(i+1,len(priorities)):
            print('i : ',i,'j :',j)
            if priorities[i] < priorities[j]:
                point_idxs.append(i)
                break
    for point_idx in point_idxs:
        w_list.append(w_list[point_idx])
        print(w_list)
    for point_idx in point_idxs:
        w_list.pop(0)
        print(w_list)

    
    answer = w_list.index(J)+1
        

    return answer


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))

```

* 채점 결과

```python
테스트 1 〉	통과 (4.22ms, 10.3MB)
테스트 2 〉	실패 (2.29ms, 10.2MB)
테스트 3 〉	실패 (런타임 에러)
테스트 4 〉	실패 (런타임 에러)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	실패 (0.52ms, 10.3MB)
테스트 7 〉	실패 (0.59ms, 10.3MB)
테스트 8 〉	실패 (3.87ms, 10.3MB)
테스트 9 〉	실패 (0.11ms, 10.3MB)
테스트 10 〉	실패 (0.35ms, 10.4MB)
테스트 11 〉	실패 (1.39ms, 10.3MB)
테스트 12 〉	실패 (런타임 에러)
테스트 13 〉	실패 (1.13ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	실패 (런타임 에러)
테스트 16 〉	실패 (0.13ms, 10.2MB)
테스트 17 〉	실패 (1.79ms, 10.3MB)
테스트 18 〉	실패 (0.06ms, 10.2MB)
테스트 19 〉	실패 (2.04ms, 10.3MB)
테스트 20 〉	실패 (런타임 에러)
```

### 실패😂

> 시간 초과....

* 2차 시도

```python
def solution(priorities, location):
    w_list = [i for i in range(len(priorities))]
    J = w_list[location]
    point_idxs = []
    for i in range(len(priorities)):
        for j in range(i+1,len(priorities)):
            if priorities[i] < priorities[j]:
                point_idxs.append(i)
                break
    for point_idx in point_idxs:
        w_list.append(w_list[point_idx])
    for point_idx in point_idxs:
        w_list.pop(0)

    
    answer = w_list.index(J)+1
        
    return answer
```

* 채점 결과

```python
테스트 1 〉	통과 (0.53ms, 10.3MB)
테스트 2 〉	실패 (0.08ms, 10.2MB)
테스트 3 〉	실패 (런타임 에러)
테스트 4 〉	실패 (런타임 에러)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	실패 (0.02ms, 10.3MB)
테스트 7 〉	실패 (0.04ms, 10.3MB)
테스트 8 〉	실패 (0.08ms, 10.3MB)
테스트 9 〉	실패 (0.02ms, 10.2MB)
테스트 10 〉	실패 (0.03ms, 10.1MB)
테스트 11 〉	실패 (0.06ms, 10.2MB)
테스트 12 〉	실패 (런타임 에러)
테스트 13 〉	실패 (0.10ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	실패 (런타임 에러)
테스트 16 〉	실패 (0.02ms, 10.3MB)
테스트 17 〉	실패 (0.12ms, 10.2MB)
테스트 18 〉	실패 (0.01ms, 10.2MB)
테스트 19 〉	실패 (0.15ms, 10.3MB)
테스트 20 〉	실패 (런타임 에러)
```

### 실패😂

* `deque`써보기!

### 🤝다른 풀이

* 찬구

```java

```
