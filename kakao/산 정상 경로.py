import heapq

def solution(n, paths, gates, summits):
    q = []
    visited = [10000001] * (n+1)
    summits.sort()
    graph = [[] for i in range(n+1)]
    for i,j,d in paths:
        graph[i].append((j,d))
        graph[j].append((i,d))
    
    for gate in gates:
        heapq.heappush(q,(0,gate))
        visited[gate] = 0
        
    while q:
        intensity, now = heapq.heappop(q)
        if now in summits or intensity > visited[now]:
            continue
        for i,d in graph[now]:
            new_intensity = max(d, intensity)
            if new_intensity < visited[i]:
                visited[i] = new_intensity
                heapq.heappush(q,(new_intensity,i))
                
    answer = [0,10000001]
    for summit in summits:
        if visited[summit] < answer[1]:
            answer[0] = summit
            answer[1] = visited[summit]
    
    return answer
