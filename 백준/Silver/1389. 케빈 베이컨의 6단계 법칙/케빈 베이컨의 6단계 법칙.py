import sys
INF=float('inf')
n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

result=[0]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        result[i]+=graph[i][j]
   
print(result.index(min(result[1:])))
