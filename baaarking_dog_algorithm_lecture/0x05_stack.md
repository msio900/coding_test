# ✏️0x05강 스택

> 영상 URL[📹](https://youtu.be/0DsyCXIN7Wg)

## 📑Contents<a id='contents'></a>

* 0x00 정의와 성질[👉🏻](#0x00)
* 0x01 기능과 구현[👉🏻](#0x01)
* 0x02 STL Stack
* 0x03 연습문제[👉🏻](#0x03)

## 0x00 정의와 성질[📑](#contents)<a id='0x00'></a>

![image-20221116165608616](images/image-20221116165608616.png)

* **FILO(First In Last Out)** : 먼저 들어간 원소가 나중에 나오게 됨
* queue, deque, stack -> **restricted structure**

### 스택의 성질

1. 원소의 추가 `O(1)`
2. 원소의 제거 `O(1)`
3. 제일 상단의 원소 확인 `O(1)`
4. 제일 상단이 아닌 나머지 원소들의 확인/변경이 원칙적으로 **불가능**

## 0x01 기능과 구현[📑](#contents)<a id='0x01'></a>

### 구현

![image-20221116170313517](images/image-20221116170313517.png)

```c++
const int MX = 1000005;
int dat[MX];
int pos = 0;
```

### push 함수

![image-20221116170503234](images/image-20221116170503234.png)

```c++
void push(int x) {
    dat[pos+1] = x;
}
```

### pop 함수

![image-20221116170613533](images/image-20221116170613533.png)

```c++
void pop(){
    pos--;
}
```

### top함수

![image-20221116170655051](images/image-20221116170655051.png)

```c++
void top(){
    return dat[pos-1];
}
```

### python으로 스택 구현하기[✏️](0x05_stack_test.py)

* 구현

  ```python
  MX = 1000005
  dat = [0] * MX
  pos = 0
  ```

* push()

  ```python
  def push(x : int):
      global pos
      dat[pos] = x
      pos += 1
  ```

* pop()

  ```python
  def pop():
      global pos
      pos -= 1
  ```

* top()

  ```python
  def top():
      return dat[pos-1]
  ```

## 0x02 STL Stack



## 0x03 연습문제[📑](#contents)<a id='0x03'></a>

### 백준 10828번 : 스택 [문제⌨️](https://www.acmicpc.net/problem/10828)

> 풀이[✏️](../acmicpc/re_10828/re_10828.md)

* stack 자료구조의 기본 기능인 `push()`, `pop()`, `top()`을 함수로 구현하여 풀이

  ```python
  import sys
  
  input = sys.stdin.readline
  
  mx = 10000005
  dat = [0]*mx
  pos = 0
  
  def push(x: int):
      global pos
      dat[pos] = x
      pos += 1
  
  def pop():
      global pos
      pos -= 1
  
  def size():
      return pos
  
  def top():
      return dat[pos - 1]
  
  n = int(input())
  
  for _ in range(n):
      command = input().split()
      if command[0] == 'push':
          push(int(command[1]))
      elif command[0] == 'pop':
          if pos == 0:
              print(-1)
          else:
              print(top())
              pop()
      elif command[0] == 'size':
          print(size())
      elif command[0] == 'empty':
          if pos == 0:
              print(1)
          else:
              print(0)
      else: # top()
          if pos == 0:
              print(-1)
          else:
              print(top())
  ```

  ![image-20221116175247126](images/image-20221116175247126.png)

