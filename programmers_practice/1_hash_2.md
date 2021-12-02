# 해시2 : 전화번호 목록

[해시2 : 전화번호 목록](https://programmers.co.kr/learn/courses/30/lessons/42577)

## 🖋️문제

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

* 구조대 : 119
* 박준영 : 97 674 223
* 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

* phone_book의 길이는 1 이상 1,000,000 이하입니다.
  - 각 전화번호의 길이는 1 이상 20 이하입니다.
  - 같은 전화번호가 중복해서 들어있지 않습니다.

### 입출력 예

| phone_book                        | return |
| --------------------------------- | ------ |
| ["119", "97674223", "1195524421"] | false  |
| ["123","456","789"]               | true   |
| ["12","123","1235","567","88"]    | false  |

### 입출력 예 설명

* 입출력 예 #1
  앞에서 설명한 예와 같습니다.

  입출력 예 #2
  한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.
  
  입출력 예 #3
  첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

---

## 💡풀이

* 풀이 1

```python
def solution(phone_book):
    answer = True
    head = phone_book[0]
    phone_book.sort()
    print(phone_book)
    for i in phone_book[1:]:
        if i[:len(head)] == head:
            answer = False
            break

    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	실패 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	실패 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	실패 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	실패 (0.27ms, 10.3MB)
테스트 15 〉	통과 (0.40ms, 10.3MB)
테스트 16 〉	실패 (0.37ms, 10.4MB)
테스트 17 〉	실패 (0.37ms, 10.4MB)
테스트 18 〉	실패 (0.70ms, 10.3MB)
테스트 19 〉	통과 (0.74ms, 10.4MB)
테스트 20 〉	실패 (1.10ms, 10.5MB)

효율성  테스트
테스트 1 〉	통과 (3.36ms, 10.8MB)
테스트 2 〉	통과 (2.94ms, 10.9MB)
테스트 3 〉	실패 (77.45ms, 30.6MB)
테스트 4 〉	통과 (86.26ms, 28.1MB)

채점 결과
정확성: 50.0
효율성: 12.5
합계: 62.5 / 100.0
```

### 실패😂

> 실패 이유 : 문제를 제대로 파악하지 못함.
>
> 주어진 번호 중 첫번째 번호가 접두어가 아님.

* 2차 시도

```python
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                answer = False

    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.3MB)
테스트 14 〉	통과 (0.45ms, 10.3MB)
테스트 15 〉	통과 (0.63ms, 10.3MB)
테스트 16 〉	통과 (0.48ms, 10.3MB)
테스트 17 〉	통과 (0.66ms, 10.3MB)
테스트 18 〉	통과 (1.01ms, 10.3MB)
테스트 19 〉	통과 (1.21ms, 10.4MB)
테스트 20 〉	통과 (1.36ms, 10.4MB)

효율성  테스트
테스트 1 〉	통과 (5.79ms, 10.8MB)
테스트 2 〉	통과 (6.51ms, 10.8MB)
테스트 3 〉	통과 (89.64ms, 30.6MB)
테스트 4 〉	통과 (108.61ms, 28.1MB)

채점 결과
정확성: 83.3
효율성: 16.7
합계: 100.0 / 100.0
```

### 성공😂

### 🤝다른 풀이

* 찬구

```java
package com.programmers.p42577;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public static void main(String[] args) {
// 1 11 119
        String[] s = {"119", "97674223", "1195524421"};
        String[] s1 = {"123","456","789"};
        String[] s2 = {"12","123","1235","567","88"};

        System.out.println(solution(s));
    }

    static public boolean solution(String[] phone_book) {
        boolean answer = true;

        Set<String> set = new HashSet<>(Arrays.asList(phone_book));

        loop:
        for (String s : phone_book) {
            for (int j = 0; j < s.length(); j++) {
                if (set.contains(s.substring(0, j))) {
                    answer = false;
                    break loop;
                }
            }
        }
        return answer;
    }
}
```

* 프로그래머스 풀이
  * `zip()`, `startswith()`함수 사용

```python
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
```

