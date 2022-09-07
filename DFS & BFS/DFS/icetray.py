n,m = map(int, input().split())
tray = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
  line = input()
  for j in range(m):
    tray[i][j] = int(line[j])

def dfs(x,y):
  if x<= -1 or x>= n or y<=-1 or y>=m:
    return False
  if tray[x][y] == 0:
    tray[x][y] = 1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1

print(result)
