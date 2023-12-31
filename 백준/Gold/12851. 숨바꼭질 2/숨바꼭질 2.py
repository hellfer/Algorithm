from collections import deque

def bfs():
    queue=deque()
    queue.append(n)
    visited[n]=0
    count[n]=1
    while queue:
        x=queue.popleft()
        for nx in [x-1,x+1,x*2]:
            if 0<=nx<100001:
                if visited[nx]==-1:
                    visited[nx]=visited[x]+1
                    count[nx]=count[x]
                    queue.append(nx)
                elif visited[nx]==visited[x]+1: 
                    count[nx]+=count[x]
#목적지가 8이라면 count[7]에 해당되는 경로는 모두 더해줌
                    
n,m=map(int,input().split())
visited=[-1]*100001
count=[0]*100001
bfs()
print(visited[m])
print(count[m])




