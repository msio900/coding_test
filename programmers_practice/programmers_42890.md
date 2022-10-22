# 후보키[↩](../programmers_practice)

[후보키](https://school.programmers.co.kr/learn/courses/30/lessons/42890)

## 🖋️문제

프렌즈대학교 컴퓨터공학과 조교인 제이지는 네오 학과장님의 지시로, 학생들의 인적사항을 정리하는 업무를 담당하게 되었다.

그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.

후보키에 대한 내용이 잘 기억나지 않던 제이지는, 정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.

- 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
  - 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
  - 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.

![cand_key1.png](https://grepp-programmers.s3.amazonaws.com/files/production/f1a3a40ede/005eb91e-58e5-4109-9567-deb5e94462e3.jpg)

위의 예를 설명하면, 학생의 인적사항 릴레이션에서 모든 학생은 각자 유일한 "학번"을 가지고 있다. 따라서 "학번"은 릴레이션의 후보 키가 될 수 있다.
그다음 "이름"에 대해서는 같은 이름("apeach")을 사용하는 학생이 있기 때문에, "이름"은 후보 키가 될 수 없다. 그러나, 만약 ["이름", "전공"]을 함께 사용한다면 릴레이션의 모든 튜플을 유일하게 식별 가능하므로 후보 키가 될 수 있게 된다.
물론 ["이름", "전공", "학년"]을 함께 사용해도 릴레이션의 모든 튜플을 유일하게 식별할 수 있지만, 최소성을 만족하지 못하기 때문에 후보 키가 될 수 없다.
따라서, 위의 학생 인적사항의 후보키는 "학번", ["이름", "전공"] 두 개가 된다.

릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.

### 제한사항

- relation은 2차원 문자열 배열이다.
- relation의 컬럼(column)의 길이는 `1` 이상 `8` 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
- relation의 로우(row)의 길이는 `1` 이상 `20` 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
- relation의 모든 문자열의 길이는 `1` 이상 `8` 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
- relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)

### 입출력 예

| relation                                                     | result |
| ------------------------------------------------------------ | ------ |
| `[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]` | 2      |

### 입출력 예 설명

**입출력 예 #1**
문제에 주어진 릴레이션과 같으며, 후보 키는 2개이다.

## 💡풀이

```python
from itertools import combinations

def solution(relation):
    x, y = len(relation[0]), len(relation) # x :num of rows y : num of columns
    col = list(range(x))    # for presenting columns cases
    cases = []
    uniques = []
    # candidate key's combination list
    for i in range(1, x + 1):
        case = list(combinations(col, i)) # 
        cases += case
    
    for case in cases: # 'case': each candidate key column
        keys = []
        for j in range(y):
            key = ''
            for i in case:
                key += relation[j][i]
            keys.append(key)
        if len(keys) == len(set(keys)): # varify uniqueness
            for x in uniques:
                if set(x).issubset(set(case)): # varify minimality
                    break
            else:
                uniques.append(list(case))

    return len(uniques)
```

* 채점 결과

```python
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.1MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.07ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.17ms, 10.2MB)
테스트 11 〉	통과 (0.15ms, 10.1MB)
테스트 12 〉	통과 (0.97ms, 10.1MB)
테스트 13 〉	통과 (0.28ms, 10.2MB)
테스트 14 〉	통과 (0.04ms, 10.1MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
테스트 16 〉	통과 (0.04ms, 10.2MB)
테스트 17 〉	통과 (0.05ms, 9.99MB)
테스트 18 〉	통과 (2.86ms, 10.1MB)
테스트 19 〉	통과 (2.75ms, 10.1MB)
테스트 20 〉	통과 (4.77ms, 10MB)
테스트 21 〉	통과 (2.71ms, 9.99MB)
테스트 22 〉	통과 (1.11ms, 10.1MB)
테스트 23 〉	통과 (0.09ms, 10.2MB)
테스트 24 〉	통과 (2.31ms, 10.3MB)
테스트 25 〉	통과 (2.44ms, 10.2MB)
테스트 26 〉	통과 (2.06ms, 10MB)
테스트 27 〉	통과 (0.26ms, 10.1MB)
테스트 28 〉	통과 (0.40ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

### 성공😂
* 이 문제는 '후보키'의 두 가지 속성인 `유일성`과 `최소성`을 만족시키는 컬럼의 조합을 찾는 문제이다.
  * 테이블이 갖는 열의 조합을 찾기 위해 `itertools` 패키지의 `combinations`함수를 사용하였다.
  * 1개부터 모든 열의 갯수까지의 조합을 도출하기 위해 `for`반복문을 `range(1, len(col) + 1)`로 구성하였다.
  * 열의 갯수가 적은 경우부터 튜플의 리스트를 만들어 다음 조건문을 통해 `유일성`을 검증한다.
    ```python
    if len(keys) == len(set(keys)):
    ```
  * 그 다음 `issubset()`함수를 사용하여 유일성이 검증된 키(key)가 기존에 나온 후보키의 부분집합이 아닌지 검증한다.
    ```python
    if set(x).issubset(set(case)):
    ```
* 최종적으로 검증된 후보키 조합을 `unique`라는 리스트에 넣었으므로 `len(uniques)`를 return하면 정답이 나온다.

### 🤝다른 풀이

