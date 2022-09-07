# DFS & BFS

탐색 알고리즘(원하는 데이터를 찾는 과정)

그래프 탐색 알고리즘으로 **코딩 테스트에서 매우 자주 등장하는 유형**

### 스택

* 먼저 들어 온 데이터가 나중에 나가는 선입후출
* 입구와 출구가 동일한 형태

```python
# 스택 구현
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```



### 큐

* 먼저 들어온 데이터가 먼저 나가는 선입선출 형식
* 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태

```python
# 큐 구현
# deque 라이브러리 사용
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력
```



### 재귀 함수

* 자기 자신을 다시 호출하는 함수

``` python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
# 파이썬은 최대 깊이 제한이 있어서 오류 메시지 출력 후 종료
# maximum recursion depth exceeded
```

* 재귀 함수를 문제 풀이에 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
* 종료 조건을 명시하지 않으면 함수가 무한히 호출됨

```python
def recursive_function(i):
    if i==100:
        return
    print(i, '번째 재귀함수에서', i+1,'번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')
    
recursive_function(1)
```



팩토리얼 구현 예제

* n! = 1 x 2 x 3 x ... x (n-1) x n
* 수학적으로 0!과 1!의 값은 1

```python
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현 : ',factorial_iterative(5))
print('재귀적으로 구현 : ',factorial_recursive(5))
```



최대공약수 계산 (유클리드 호제법) 예제

* 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있습니다.
* 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 합시다.
* 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.

``` python
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
    
print(gcd(192,162))
```



이와 같이 재귀함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있으나, 어려운 형태의 코드가 되지 않도록 신중하게 사용해야 하고, 반복문에 대비한 장단점을 따진 후 상황에 맞게 사용해야 한다.

컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓이는데, 스택을 사용해야 할 때 구현상 스택 라이브러리 대신 재귀 함수를  사용할 수 있음.
