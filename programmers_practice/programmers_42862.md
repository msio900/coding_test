## 체육복[↩](../programmers_practice)

> [체육복](https://programmers.co.kr/learn/courses/30/lessons/42840)

## 🖋️문제

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 전체 학생의 수는 2명 이상 30명 이하입니다.
- 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
- 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

### 입출력 예

| n    | lost   | reserve   | return |
| ---- | ------ | --------- | ------ |
| 5    | [2, 4] | [1, 3, 5] | 5      |
| 5    | [2, 4] | [3]       | 4      |
| 3    | [3]    | [1]       | 2      |

### 입출력 예 설명

- 예제 #1
  1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

- 예제 #2
  3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.

### 1차 시도

```python
def solution(n, lost, reserve):
    students = [i for i in range(1, n+1) if i not in lost] # 수업을 들을 수 있는 학생의 출석번호로 구성된 리스트 만들어 줌.
    for i in lost: # 체육복을 도난당한 번호대로 for문으로 추출
        if (i - 1) in reserve: # 앞 번호가 있는지 확인
            students.append(reserve.pop(reserve.index(i - 1))) # 있으면 빌려줌
        elif (i + 1) in reserve: # 뒷번호가 있는지 확인
            students.append(reserve.pop(reserve.index(i + 1))) # 있으면 빌려줌

    answer = len(students)
    return answer
```

* 채점 결과

```python
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	실패 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	실패 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	실패 (0.01ms, 10.2MB)
테스트 13 〉	실패 (0.01ms, 10.3MB)
테스트 14 〉	실패 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
채점 결과
정확성: 75.0
합계: 75.0 / 100.0
```

### 실패😂
* `lost`에도 있고, `reserve`에도 있는 경우를 감안하지 못함.

### 2차 시도

```python
def solution(n, lost, reserve):
    students = [i for i in range(1, n+1) if i not in lost]
    for i in lost:
        if i in reserve: # 본인의 것은 잃어버렸으나 여벌의 옷을 챙긴 경우를 추가
            students.append(reserve.pop(reserve.index(i)))
        elif (i - 1) in reserve:
            students.append(reserve.pop(reserve.index(i - 1)))
        elif (i + 1) in reserve:
            students.append(reserve.pop(reserve.index(i + 1)))

    answer = len(students)
    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	실패 (0.01ms, 10.2MB)
테스트 13 〉	실패 (0.01ms, 10.2MB)
테스트 14 〉	실패 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 85.0
합계: 85.0 / 100.0
```

### 실패😂

* `lost`에도 있고, `reserve`에도 있는 경우를 감안하지 못함.

### 3차 시도

> 정화님 코드 참고

```python
def solution(n, lost, reserve):
    answer = n

    new_lost = [l for l in lost if l not in reserve]
    new_lost.sort()
    new_reserve = [l for l in reserve if l not in lost]
    new_reserve.sort()

    for l in new_lost:
        if l - 1 in new_reserve:
            new_reserve.remove(l - 1)
        elif l + 1 in new_reserve:
            new_reserve.remove(l + 1)
        else:
            answer -= 1

    return answer
```

* 채점 결과

```python
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10MB)
테스트 10 〉	통과 (0.01ms, 10MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

## 다른 풀이

```python

```
## 성공😊
```python

```