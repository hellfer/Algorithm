from collections import deque

dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=0
                
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
count=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            bfs(i,j)
            count+=1
            
print(count)