from queue import PriorityQueue
n,m=map(int, input().split())
graph=[[]*(n+1) for _ in range(n+1)]
indegree=[0]*(n+1)
for i in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    indegree[y]+=1
      
def topology():
    result=[]
    queue=PriorityQueue()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.put(i)
    while not queue.empty():
        a=queue.get()
        result.append(a)
        for i in graph[a]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.put(i)
    for i in result:
        print(i,end=' ')
topology()