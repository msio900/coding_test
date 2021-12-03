# 해시3 : 위장

[해시3 : 위장](https://programmers.co.kr/learn/courses/30/lessons/42578)

## 🖋️문제

스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

| 종류 | 이름                       |
| ---- | -------------------------- |
| 얼굴 | 동그란 안경, 검정 선글라스 |
| 상의 | 파란색 티셔츠              |
| 하의 | 청바지                     |
| 겉옷 | 긴 코트                    |

스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
- 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
- 같은 이름을 가진 의상은 존재하지 않습니다.
- clothes의 모든 원소는 문자열로 이루어져 있습니다.
- 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
- 스파이는 하루에 최소 한 개의 의상은 입습니다.

### 입출력 예

##### 입출력 예

| clothes                                                      | return |
| ------------------------------------------------------------ | ------ |
| [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]] | 5      |
| [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]] | 3      |

### 입출력 예 설명

* 예제 #1
  headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로 아래와 같이 5개의 조합이 가능합니다.

```
1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses
```

* 예제 #2
  face에 해당하는 의상이 crow_mask, blue_sunglasses, smoky_makeup이므로 아래와 같이 3개의 조합이 가능합니다.

```
1. crow_mask
2. blue_sunglasses
3. smoky_makeup
```

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

