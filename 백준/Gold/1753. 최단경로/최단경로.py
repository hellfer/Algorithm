import sys
import heapq
input=sys.stdin.readline

INF=float('inf')

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
visited=[False]*(n+1)
start=int(input())

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    queue=[]
    distance[start]=0
    visited[start]=True
    heapq.heappush(queue,(0,start))
    while queue:
        a,b=heapq.heappop(queue)
        if distance[b]<a:
            continue
        for i in graph[b]:
            cost=a+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(queue,(cost,i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])