# 정렬2 : 가장 큰 수[↩](../programmers_practice)

[힙(Heap)2 : 디스크 컨트롤러](https://programmers.co.kr/learn/courses/30/lessons/42627)

## 🖋️문제

 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

### 입출력 예

| numbers           | return    |
| ----------------- | --------- |
| [6, 10, 2]        | "6210"    |
| [3, 30, 34, 5, 9] | "9534330" |

## 💡풀이

### 1차 시도

```python

```

* 채점 결과

```python

```

### 실패😂

* 

### 2차 시도😂

```python

```

* 채점 결과

```python

```

### 실패😂

* 시간 초과

### 🤝다른 풀이

* 찬구

```java
package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * Date: 2021-12-17
 * Time: 11:50
 * https://www.acmicpc.net/problem/1935
 */
public class Stack1935_후위표기식2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        char[] charArray = br.readLine().toCharArray();

        double[] numbers = new double[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = Double.parseDouble(br.readLine());
        }

        Stack<Double> stack = new Stack<>();
        for (int c : charArray) {
            if (c >= 'A') {
                stack.push(numbers[c - 'A']);
            } else {
                double y = stack.pop();
                double x = stack.pop();

                switch (c) {
                    case '*': stack.push(x * y); break;
                    case '+': stack.push(x + y); break;
                    case '-': stack.push(x - y); break;
                    case '/': stack.push(x / y); break;
                }
            }
        }

        System.out.printf("%.2f%n", stack.pop());
        br.close();
    }
}
```

* 준오

```java
def solution(numbers):
    numbers.sort(key = lambda x : str(x) * 3, reverse = True)
    return str(int("".join(list(map(str, numbers)))))
```
파이썬은 3줄만에 가능한 문제.
1. 파이썬의 숫자로 구성된 문자열은 맨 앞자리부터 비교하는 습성이 있다. 맨 앞자리부터 비교해 숫자가 크면 더 큰 문자열로 정렬해준다는 의미

   ex. 11과 9를 비교하게 되면 숫자 자체는 11이 크나 파이썬은 1(십의 자리)과 9(일의 자리)를 비교하기 때문에 9가 11보다 큰 걸로 인식됨.

   Q. 그러면 두번째 예시인 3과 30은 어떻게 비교하나여?
   A. 3과 30을 정렬하면, 문제의 요구에 따라 303이 아닌 330이 되어야 하므로 3을 30보다 더 큰 숫자로 정렬해 주어야 하는데, 이 두 숫자를 비교하기 위해서는(즉, 정렬하기 위해서는) 각 자리를 3배씩 늘려줘야 함. 문자열에 *3을 해주어 '333'과 '303030'을 만들어 주면, 앞에서 두번째 자리에서의 비교를 통해 '333'이 '303030'보다 더 큰 문자열로 정렬해 줄 수 있음.   

2. sort()에 대해 더 깊은 이해도가 필요함. 나도 옛날에 유튜브 '나도코딩'님꺼로 공부했던 것이 생각나서 그거대로 코딩.

   나를 포함한 많은 이들이 보통 리스트의 요소를 정렬하기 위해 단순히 .sort()로만 사용하는데, sort의 내부 키워드인 key를 이용해 리스트의 각 요소에 조건을 걸어 정렬할 수 있고, 기본적으로 오름차순으로 정렬해주는 sort의 결과를 따로 역순으로 만들 필요 없이 reverse 키워드를 이용 가능. 그 결과가 바로 두 번째 줄에 나오는 람다 함수. 여기서는 또 동빈나의 강의가 빛을 발했는데 람다 함수를 통해 리스트의 요소에 접근하는 듯 하는 예제가 있었기 때문에 이를 응용. 람다는 숨 쉬듯이 쓸 줄 알아야 할 것 같다. 두 번째 줄처럼 쓰면, key 키워드에 람다 함수를 이용해 각 문자열을 3배씩 늘려 비교한 것을 역순으로 정렬하므로 정확히 우리가 원하는 리스트를 결과로 얻을 수 있다.

3. 한국인은 삼세판이라서 세번째는...아니고 이거 안해주면 오류 난다. 나도 씐나게 두 줄로 끝나는 줄 알고 설레발 치다가 뻑났다.

   리스트가 [0, 0, 0, 0] 과 같이 모두 0일 때 자리수가 늘어나지 않고 0이 되어야 하는 것을 고려해 문자열로 만들어진 것을 정수로 한번 변환하고, 다시 문자열로 변환해야 한다. 

   만약 위처럼 [0, 0, 0, 0]이 입력으로 주어지면 문자열로 변환했을 때 '0000'일 것이고 이는 정수로 그냥 0이다. 따라서 '0'으로 바꿔주기 위해 추가해야 하는 것이

   str(int("".join(list(map(str, numbers))))). 바로 세 번째 줄 코드

   Q. 아니 무슨 SQL도 아니고 join은 왜 썼나여? 바보인가여?(실제로 제 친구한테 3줄짜리 코드 자랑하려고 코드 보여줬더니 친구가 했던 말)
   -> ?. 그냥 문자열 합쳐주려고 쓴 거다. 파알못 saeki.
