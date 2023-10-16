n=int(input())
m=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
count=0
for i in range(m) :
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
    
def dfs(v) :
    global count
    visited[v]=1
    count+=1
    for i in range(1, n+1) :
        if not visited[i] and graph[v][i] :
             dfs(i)
                
start_node=1
dfs(start_node)
print(count-1)