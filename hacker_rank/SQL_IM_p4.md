# 📝SQL IM Problem4 : Weather Observation Station 20[↩](../)

> 문제 URL [🔗](https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=false)

A *[median](https://en.wikipedia.org/wiki/Median)* is defined as a number separating the higher half of a data set from the lower half. Query the *median* of the *Northern Latitudes* (*LAT_N*) from **STATION** and round your answer to decimal places.

**Input Format**

The **STATION** table is described as follows:

![Station.jpg](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where *LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## ✏️정답

### 1차 시도

```mysql
SET @IDX=-1;
SELECT ROUND(AVG(LAT_N), 4) AS MEDIAN
FROM (SELECT 
        @IDX := @IDX + 1 AS IDX,
        LAT_N 
      FROM STATION 
      ORDER BY LAT_N) SUB
WHERE IDX IN (FLOOR(@IDX / 2), CEIL(@IDX / 2))
```

### 성공😊

![image-20221213113605688](images/image-20221213113605688.png)

* 이 문제는 `MySQL`에는 없는 중위수(median)을 출력하도록 하는 문제

* **중위수(median)**는 어떤 주어진 값들을 크기의 순서대로 정렬했을때 가장 중앙에 위치한 값을 의미, 값이 짝수개일 때에는 중앙값이 두 개 이므로 두 값의 평균을 취함.

* `MySQL`에서는 `python`의 데이터프레임과는 달리 인덱스를 별도로 만들어주어야 함. 따라서 쿼리문에서 변수를 생성하게 하는 명령어인 `SET`을 사용함. 

  * `SET`을 통해 변수 생성

    ```mysql
    SET @IDX=-1;
    ```

  * 서브쿼리에 `LAT_N`컬럼의 오름차순으로 테이블을 정렬하고 `@IDX := @IDX + 1 AS IDX`인덱스 생성

    ```mysql
    FROM (SELECT 
            @IDX := @IDX + 1 AS IDX,
            LAT_N 
          FROM STATION 
          ORDER BY LAT_N) SUB
    ```

    여기서 유의할 점은 `FROM`에서 서브쿼리를 사용할 경우 alias를 반드시 해야함

* 중위수는 데이터의 행의 갯수가 홀수일 경우 데이터의 배열중 가운데 수를 나타내고 짝수일 경우 가운데 두 수의 평균을 나타내야 하므로 WHERE절을 다음과 같이 정의함.

  ```mysql
  WHERE IDX IN (FLOOR(@IDX / 2), CEIL(@IDX / 2))
  ```

  >  `FLOOR`는 버림을 실행하는 명령어, `CEIL`은 올림을 실행하는 명령어 

  * 총 갯수가 홀수일 경우, `IDX`를 2로 나누면 나누어 떨어져 **중위수**의 위치가 나옴
  * 총 개수가 짝수일 경우,  `IDX`를 2로 나누면 중앙의 위치가 나오게 되고 `FLOOR()` 명령과 `CEIL()`명령을 통해 중위수 두 값을 출력할 수 있음.

* 전체 행의 개수가 홀수일 경우 중위수는 가운데 값이기 때문에 `AVG()`는 중위수를 도출

* 전체 행의 개수가 짝수일 경우 가운데에 있는 수가 2개이기 때문에 `AVG()` 명령을 통해 두 수의 평균으로 중위수를 도출