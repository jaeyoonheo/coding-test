# 이진 탐색

* 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
* 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법

시간 복잡도 : 연산 횟수는 log N에 비례

예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1 단계를 거치면 16개의 데이터만 남습니다.

즉, 범위를 절반씩 줄이며 시간 복잡도는 O(log N)을 보장합니다.



```python
# 이진 탐색 소스코드의 재귀적 구현
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    
n, target = map(int, input().split())
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```



### 파이썬 이진 탐색 라이브러리

* bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
* bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

``` python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1.2.3.3.3.3.4.4.8.9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

# 실행 결과 2
# 실행 결과 6
```



### 파라메트릭 서치

파라메트릭 서치란 최적화 문제를 결정 문제로 바꾸어 해결하는 기법 (일반적으로 이진 탐색 사용)

