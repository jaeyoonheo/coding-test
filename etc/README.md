# 기타 알고리즘

### 소수 판별

* 소수란 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수
  * 6은 1, 2, 3, 6으로 나누어 떨어지므로 소수가 아닙니다.
  * 7은 1과7을 제외하고는 나누어떨어지지 않으므로 소수입니다.
* 코딩 테스트에서는 어떠한 자연수가 소수인지 아닌지 판별해야 하는 문제가 자주 출제됩니다.

2부터 X-1까지의 모든 자연수에 대해서 연산을 수행해야 한다.
모든 수를 하나씩 확인하기 때문에 시간 복잡도는 O(X)

**약수의 성질**

* 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭

```python
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
        return True
print(is_prime_number(4)) # False
print(is_prime_number(7)) # True
```

시간 복잡도는 O(N^0.5)

**다수의 소수 판별**

* 특정한 수 범위 안에 존재하는 모든 소수를 찾을 때 에라토스테네스의 체 알고리즘 사용 가능
* N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.
* 동작 과정
  1. 2부터 N까지의 모든 자연수를 나열
  2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
  3. 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
  4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

```python
import math

n = 1000
array = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if array[i] == True:
        j=2
        while i*j <= n:
            array[i*j] = False
            j+=1
            
for i in range(2, n+1):
    if array[i]:
        print(i,end = ' ')
```

시간 복잡도는 O(N log log N)  하지만 메모리가 많이 필요하다.



### 투 포인터

* 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘
* 2, 3, 4, 5, 6, 7번 학생을 지목해야 할 때 간단히 '2번부터 7번까지의 학생'이라고 부른다.
* 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 시작점과 끝점 2개의 점으로 접근할 범위를 지정

**특정한 합을 가지는 부분 연속 수열 찾기**

* N개의 자연수로 구성된 수열
* 합이 M인 부분 연속 수열의 개수

* 문제 해결
  1. 시작점과 끝점이 첫 번째 원소의 인덱스를 가리키도록 한다.
  2. 현재 부분 합이 M과 같다면, 카운트한다.
  3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다.
  4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다.
  5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.

```python
n = 5
m = 5
data = [1,2,3,4,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end +=1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
    
print(count)
```



### 구간 합

* 구간 합 문제 : 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
* 예를 들어 5개의 데이터로 구성된 수열 {10,20,30,40,50}이 있다고 가정할 때
  두 번째 수부터 네 번째 수까지의 합은 20 + 30 + 40 = 90 입니다.
* 접두사 합 : 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
  * N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P에 저장합니다.
  * 매 M개의 쿼리 정보를 확인할 때 구간 합은 P[Right] - P[Left-1]입니다.

```python
n = 5
data = [10,20,30,40,50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1])
```

