from collections import deque

def solution(maps):
    global answer, visited
    
    row, col = len(maps), len(maps[0])
    dic = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    table = [[-1]*col for _ in range(row)]
    table[0][0] = 1
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]

            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] != 0:
                if table[nx][ny] == -1:
                    table[nx][ny] = table[x][y] + 1     
                    q.append([nx, ny])

    return table[-1][-1]
