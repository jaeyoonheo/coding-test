# 최단 경로 문제

* 최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미합니다.
* 다양한 문제 상황
  * 한 지점에서 다른 한 지점까지의 최단 경로
  * 한 지점에서 다른 모든 지점까지의 최단 경로
  * 모든 지점에서 다른 모든 지점까지의 최단 경로
* 각 지점은 그래프에서 노드로 표현
* 지점 간 연결된 도로는 그래프에서 간선으로 표현



### 다익스트라 최단 경로 알고리즘

* 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산합니다.
* 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작합니다.
  * 현실 세계의 간선은 음의 간선으로 표현되지 않습니다.
* 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류됩니다.
  * 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.

* 알고리즘의 동작 과정
  1. 출발 노드를 설정합니다.
  2. 최단 거리 테이블을 초기화합니다.
  3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택합니다.
  4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신합니다.
  5. 위 과정에서 3번과 4번을 반복합니다.

``` python
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[]for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

시간복잡도는 O(V^2)으로 노드의 개수가 5000개 이하라면 이 코드로 문제 해결 가능



### Priority Queue

* 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
* 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐 이용 가능
* 표준 라이브러리 형태로 지원
* 이를 구현하기 위해 **Heap**을 사용할 수 있음
* 최소 힙과 최대 힙이 있으며, 삽입 / 삭제에 O(log N) 소모

```python
# 최소 힙
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heqppush(h,value)
        # 최대 힙을 사용하고자 한다면 value 대신 -value 사용
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
# 실행결과 [0,1,2,3,4,5,6,7,8,9]
```

방문하지 않은 노드 중 가장 짧은 노드를 선택하기 위해 힙 자료구조 사용하면 실행시간 개선 가능



```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[]for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
```

시간 복잡도는 O(ElogV)

반복문은 노드의 개수 이상의 횟수로는 처리되지 않고, 중복간선을 포함하지 않으면 

**O(ElogE) = O(ElogV^2) = O(ElogV)**



### 플로이드 워셜 알고리즘

* 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
* 다익스트라와 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행
  * 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다.
* 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장
* 다이나믹 프로그래밍 유형에 속한다.
* 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인
  * a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로가는 거리가 더 짧은지 검사
* 점화식 D_ab = min(D_ab, D_ak + D_kb)

```python
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY",end=" ")
        else:
            print(graph[a][b], end=" ")
	print()
```

총 시간 복잡도는 O(N^3)

