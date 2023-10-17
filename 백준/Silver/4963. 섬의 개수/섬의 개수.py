from collections import deque

dx = [-1, -1, -1, 0, 0, 1 ,1 ,1]
dy = [-1 ,0 ,1 ,-1 ,1 ,-1 ,0 , 1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            if not visited[nx][ny] and graph[nx][ny]==1:
                visited[nx][ny]=True
                queue.append((nx,ny))

while True:
    m,n=map(int,input().split())
    
    if n==0 and m==0:
        break
    
    graph=[]
    
    for _ in range(n):
        a=list(map(int,input().split()))
        graph.append(a)
    
    visited=[[False]*m for _ in range(n)]
    
    count=0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]==1:
                bfs(i,j)
                count+=1
                
    print(count)



                
            