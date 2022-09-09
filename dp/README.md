# 다이나믹 프로그래밍

* 다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
* 이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다.
* 다이나믹 프로그래밍의 구현은 일반적으로 탑다운 / 바텀업 방식으로 구성
* 다이나믹 프로그래밍을 사용하는 경우
  1. 최적 부분 구조
     - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있습니다.
  2. 중복되는 부분 문제
     - 동일한 작은 문제를 반복적으로 해결해야 합니다.

ex) 피보나치 수열

```python
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))
```

재귀를 사용하면 중복 호출되는 입력값이 있기 때문에 **O(2^n)**



### 메모이제이션

메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나

한 번 계산한 결과를 메모 / 값을 기록해 놓는다는 점에서 캐싱이라고도 함

전형적인 다이나믹 프로그래밍은 바텀업 방식 메모이제이션은 탑다운 방식

``` python
# 메모이제이션(탑다운)
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
```

```python
# 바텀업
d = [0] * 100

d[1] = 1
d[2] = 2
n = 99

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])
```

이를 사용하면 O(N)만에 처리 가능



### 분할 정복과의 차이

분할 정복의 대표격 : 퀵 정렬(피봇의 좌우로 구분)

부분 문제가 중복된다 - 다이나믹 프로그래밍 / 중복되지 않는다 - 분할 정복



### 접근 방법

* 그리디, 구현, 완전 탐색의 아이디어로 문제를 해결할 수 있는지 검토하고 방법이 떠오르지 않으면 다이나믹 프로그래밍을 고려
* 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법 사용
* 기본 유형으로 출제되는 경우가 많다
