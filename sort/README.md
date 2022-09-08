# 정렬

데이터를 특정한 기준에 따라 순서대로 나열하는 것

일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다.



### 선택 정렬

처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        
print(array)
# 실행결과 [0,1,2,3,4,5,6,7,8,9]
```

시간 복잡도 : O(N^2)



### 삽입 정렬

처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입

선택 정렬에 비해 구현 난이도가 높은 편, 일반적으로 더 효율적으로 동작

```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
            
print(array)
# 실행 결과 [1,2,3,4,5,6,7,8,9]
```

시간 복잡도 : O(N^2)

현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작

최선의 경우 O(N)



### 퀵 정렬

기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈

일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘

병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간

기본적인 퀵 정렬은 **첫 번째 데이터를 기준(Pivot)으로 설정**

시간 복잡도 : 퀵 정렬은 평균 O(NlogN)의 시간 복잡도를 가진다.

최악의 경우 O(N^2)

```python
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
	if start>= end:
    	return
	pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left>right):
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[right] = array[right], array[left]
            
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
# 실행 결과 [0,1,2,3,4,5,6,7,8,9]
```

```python
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array
   	pivot = array[0]
    tail  = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
# 실행 결과 [0,1,2,3,4,5,6,7,8,9]
```



### 계수 정렬

특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘

데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을  때 사용 가능

데이터의 개수가 N, 데이터 중 최댓값이 K일 떄 최악의 경우에도 수행 시간 O(N + K)를 보장

```python
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
        
# 실행 결과 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```

시간 복잡도와 공간 복잡도 모두 O(N + K)

데이터가 양극화가 심하면 비효율적이다.

동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적

| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 | 특징                                                         |
| ------------- | ---------------- | ----------- | ------------------------------------------------------------ |
| 선택 정렬     | O(N^2)           | O(N)        | 아이디어가 매우 간단                                         |
| 삽입 정렬     | O(N^2)           | O(N)        | 데이터가 거의 정렬되어 있을 때 가장 빠름                     |
| 퀵 정렬       | O(NlogN)         | O(N)        | 대부분의 경우에 가장 적합하고, 빠름                          |
| 계수 정렬     | O(N+K)           | O(N+K)      | 데이터의 크기가 한정되어 있을 경우에 사용 가능하지만 매우 빠름 |

