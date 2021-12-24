# 완전탐색(BFS) 3 : 카펫[↩](../programmers_practice)

[완전탐색(BFS) 3 : 카펫](https://programmers.co.kr/learn/courses/30/lessons/42842)

## 🖋️문제

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

![carpet.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b1ebb809-f333-4df2-bc81-02682900dc2d/carpet.png)

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

### 입출력 예

| brown | yellow | return |
| ----- | ------ | ------ |
| 10    | 2      | [4, 3] |
| 8     | 1      | [3, 3] |
| 24    | 24     | [8, 6] |

## 💡풀이


```python
def solution(brown, yellow):
    answer = []
    stack = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            stack.append(i)
    print(stack)
    for j, i in zip(range(len(stack)), reversed(range(len(stack)))):
        if 2*stack[i]+2*stack[j]+4 == brown:
            a, b = stack[i], stack[j]
            break
    answer = [a+2, b+2]


    return answer
```

* 채점 결과

```python
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (56.71ms, 10.2MB)
테스트 4 〉	통과 (0.15ms, 10.2MB)
테스트 5 〉	통과 (0.50ms, 10.3MB)
테스트 6 〉	통과 (17.44ms, 10.2MB)
테스트 7 〉	통과 (67.56ms, 10.3MB)
테스트 8 〉	통과 (55.63ms, 10.3MB)
테스트 9 〉	통과 (65.04ms, 10.3MB)
테스트 10 〉	통과 (76.75ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```

### 성공😂

### 🤝다른 풀이

* 프로그래머스 풀이

```python
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
```

* 찬구

```java

```

* 준오

```python

```

* 경현

```java
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        
        //i는 세로 갯수
        for(int i = 1; i <= brown / 2; i++){
            int row = brown - i*2; // (전채갯수 - 세로갯수*2) => 가로개수
            if(row % 2 == 0) {
                answer = new int[]{row/2, i+2};
                if(answer[0]*answer[1] == yellow+brown)
                    break;
            }
            
        }
        
        return answer;
    }
}
```

* 숙영

```python
def solution(brown, yellow):
    answer=[]

    for i in range(brown):
      j = 0
      j = brown/2-i+2
      if (i-2)*(j-2)==yellow:
        answer.append(int(j))
        answer.append(int(i))
        break
    return answer
```

