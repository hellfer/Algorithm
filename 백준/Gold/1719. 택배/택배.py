INF=float('inf')
n,m=map(int,input().split())
graph=[ [INF] * (n+1) for _ in range(n+1)]
result=[ ['-'] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x][y]=z
    graph[y][x]=z
    result[x][y]=str(y)
    result[y][x]=str(x)
  
for i in range(1,n+1):
    graph[i][i]=0
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]
                result[i][j]=result[i][k]
                
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('-',end=' ')
        else:
            print(result[i][j], end=' ')
    print()
