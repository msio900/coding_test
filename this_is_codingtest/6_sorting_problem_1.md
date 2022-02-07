# Q2. 위에서 아래로[↩](../this_is_codingtest)

| 난이도 | 풀이 시간 | 시간 제한 | 메모리 제한 |
| ------ | --------- | --------- | ----------- |
| ●○○    | 15분      | 1초       | 12MB        |

## 🖋️문제
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수 부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

### 입력
* 첫째 줄에 수열에 속해 있는수의 개수 N이 주어진다. (1 ≤ N ≤ 500) 
* 둘째 줄부터 N + 1 번째 줄까지 이개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의 자연수 이다.

### 출력
* 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서 는 자유롭게 출력해도 괜찮다.

### 예제 입력 & 출력

```python
in[0]
3
15
27
12


out[0]
27 15 12
```

---

## 💡풀이
```python
import sys

N = int(sys.stdin.readline())
list = []
for _ in range(N):
    list.append(int(sys.stdin.readline()))

print(sorted(list, reverse=True))
```
* 성공😊
  * 파이썬 기본 정렬 라이브러리 사용
  * `join`을 쓰는 것을 까먹음
  * 채원님 코멘트 : `join`을 쓰기보다는 `for문`으로 돌릴 것!

#### 나동빈님 풀이[📌](https://github.com/ndb796/python-for-coding-test/blob/master/6/10.py)

```python
# N 입력 받기
n = int(input())

# N개의 정수를 입력 받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 정렬 라이브러리를 이용하여 내림차순 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
    print(i, end=' ')
```

* 
