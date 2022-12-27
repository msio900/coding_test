# ✏️0x1C강 플루이드 알고리즘

> 영상 URL[📹](https://youtu.be/dDDy2bEZRA8)

## 📑Contents<a id='contents'></a>

* 0x00 알고리즘 설명 [👉🏻](#0x00)
* 0x01 구현 [👉🏻](#0x01)
* 0x02 경로 복원 방법 [👉🏻](#0x02)

## 0x00 알고리즘 설명 [📑](#contents)<a id='0x00'></a>

![image-20221226174106849](images/image-20221226174106849.png)

* 주어진 그래프에서 간선 옆에 적힌 값들은 **간선의 거리**(**비용**이라고도 부름)를 말함.
* 왼쪽 그림에서 3에서 1로 혹은 1에서 3으로 가는 최단 거리는 1
* 오른쪽 그림에서 3에서 5로 가는 최단거리는 얼핏 15로 보이나 3-1-4-5순으로 경로를 가게 되면 8로 최단 거리는 8

### `플로이드 알고리즘` = `모든 정점 쌍 사이의 최단 거리`를 구하는 알고리즘

![image-20221226174433933](images/image-20221226174433933.png)

* 테이블에서 당장 채울수 있는 것만 빈테이블에 채우게 되면 다음과 같음.
  ![image-20221226174604979](images/image-20221226174604979.png)

  * 자기 자신으로 가는 것은 거리가 0
  * 간선 1개로 바로 넘어갈 수 있는 것은 간선의 거리로 바로 채움
  * 바로 넘어갈 수 없는 노드는 `무한`으로 처리

* 플로이드 알고리즘은 현재 테이블에서 노드 특정 노드 번호를 거치는 방법과 대조하여 최소값을 테이블에 입력(다음은 노드1을 거치는 거리와 비교하여 최소값을 입력)

  ![image-20221226174938678](images/image-20221226174938678.png)

  * `D[s][t]` >`D[s][1] + D[1][t]` 인 경우를 입력  

* 다음은 노드2를 거치는 거리와 비교하여 최소값을 입력

  ![image-20221226175229263](images/image-20221226175229263.png)

* 노드3

  ![image-20221226175329225](images/image-20221226175329225.png)

* 노드4

  ![image-20221226175345471](images/image-20221226175345471.png)

* 노드5

  ![image-20221226175358926](images/image-20221226175358926.png)

### 시간복잡도 : `O(v^3)`

## 0x01 구현 [📑](#contents)<a id='0x01'></a>

### 백준 11404번 : 플로이드 [문제⌨️](https://www.acmicpc.net/problem/11404)

> 풀이[✏️](../acmicpc/11404/11404.md)

* 바킹독님 풀이

    ```C++
    // Authored by : BaaaaaaaaaaarkingDog
    // Co-authored by : -
    // http://boj.kr/610baea46f8d403fa58b632b29389ae1
    #include <bits/stdc++.h>
    using namespace std;

    const int INF = 0x3f3f3f3f;
    int d[105][105];
    int n, m;

    int main(void){
      ios::sync_with_stdio(0);
      cin.tie(0);

      cin >> n >> m;
      for(int i = 1; i <= n; i++)
        fill(d[i], d[i]+1+n, INF);
      while(m--){
        int a,b,c;
        cin >> a >> b >> c;
        d[a][b] = min(d[a][b], c);
      }
      for(int i = 1; i <= n; i++) d[i][i] = 0;

      for(int k = 1; k <= n; k++)
        for(int i = 1; i <= n; i++)
          for(int j = 1; j <= n; j++)
            d[i][j] = min(d[i][j], d[i][k]+d[k][j]);

      for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
          if(d[i][j] == INF) cout << "0 ";
          else cout << d[i][j] << ' ';
        }
        cout << '\n';
      }
    }
    ```

* python 풀이

  ```python
  import sys
  
  input = sys.stdin.readline
  
  n = int(input())
  matrix = [[100000000]*n for _ in range(n)]
  
  for _ in range(int(input())):
      x, y, cost = map(int, input().split())
      matrix[x-1][y-1] = min(matrix[x-1][y-1], cost)
  
  for i in range(n):
      matrix[i][i] = 0
  
  for s in range(n):
      for i in range(n):
          for j in range(n):
              if i != s or j != s:
                  matrix[i][j] = min(matrix[i][s]+matrix[s][j], matrix[i][j])
  
  for i in range(n):
      for j in range(n):
          print(0 if matrix[i][j] == 100000000 else matrix[i][j], end=' ')
      print()
  ```
  
  

## 0x02 경로 복원 방법 [📑](#contents)<a id='0x02'></a>