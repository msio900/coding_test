# Q04. 만들수 없는 금액[↩](../this_is_codingtest)

## 🖋️문제
 동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있습니다. 이때 N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.
 예를 들어, N = 5이고, 각 동전이 각각 3원, 2원, 1 원, 1원, 9원짜리 （화폐 단위） 동전이라고 가정합시다. 이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 8원입니다.
 또 다른 예시로, N = 3이고, 각 동전이 각각 3원, 5원, 7원짜리 （화폐 단위） 동전이라고 가정합시다. 이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 1원입니다.

### 입력
* 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N0| 주어집니다. （1 <N< 1,000）
* 둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분합니다. 이때, 각 화폐 단위는 1,000,000 이하의 자연수입니다.

### 출력
* 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력합니다.

### 예제 입력

```python
in[0]
5
3 2 1 1 9

out[0]
8

```

---

## 💡풀이
```python
import sys

N = int(sys.stdin.readline())
coins = sys.stdin.readline().split()

coins = [int(i) for i in coins]

print(coins)
coins.sort()
print(coins)

stack = []
for i in range(len(coins)):
 for j in range(i+1, len(coins)+1):
  stack.append(sum(coins[i:j]))
print(list(set(stack)))

not_list = [i for i in range(1, max(stack))]
print(not_list)

for i in stack:
 if i in not_list:
  not_list.remove(i)

not_list.sort()

print(not_list[0])

```

* 나동빈님 풀이

```python
n = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1
for x in data:
 # 만들 수 없는 금액을 찾았을 때 반복 종료
 if target < x:
  break
 target += x
# 만들 수 없는 금액 출력
print(target)
```

