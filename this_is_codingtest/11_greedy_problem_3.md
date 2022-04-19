# Q01. 문자열 뒤집기[↩](../this_is_codingtest)

> [백준 1493 : 뒤집기](https://www.acmicpc.net/problem/1439)

| 시간 제한 | 메모리 제한 | 제출  | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :---- | :--- | :-------- | :-------- |
| 2 초      | 128 MB      | 15227 | 8163 | 6406      | 53.428%   |

## 🖋️문제
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

예를 들어 S=0001100 일 때,

1. 전체를 뒤집으면 1110011이 된다.
2. 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.

하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.

### 입력

* 첫째 줄에 문자열 S가 주어진다. S의 길이는 100만보다 작다.

### 출력
* 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력한다.

### 예제 입력

```python
in[0]
0001100

out[0]
1

in[1]
11111

out[1]
0

in[2]
00000001

out[2]
1

in[3]
11001100110011000001

out[3]
4

in[4]
11101101

out[4]
2
```

---

## 💡풀이
```python
change = 0
prev = '?'
string = input()
for i in string:
    if i != prev: change += 1
    prev = i
print(change//2)
```

* 나동빈님 풀이

```python
data = input()
count0 = 0
count1 = 0

if data[0] =='1':
    count0 += 1
else:
    count1 += 1
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))
```
