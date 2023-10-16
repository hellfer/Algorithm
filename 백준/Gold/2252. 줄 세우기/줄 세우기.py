from collections import deque
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    indegree[y] += 1
def topology():
    queue = deque()
    result = []
    for i in range(1,n+1):
        if indegree[i] == 0: # '==' 대신 '='를 사용하였고, '1' 대신 '0'을 사용했습니다.
            queue.append(i)
    while queue:
        a = queue.popleft()
        result.append(a)
        for i in graph[a]:
            indegree[i] -= 1
            if indegree[i] == 0: # '==' 대신 '='를 사용하였고, '1' 대신 '0'을 사용했습니다.
                queue.append(i)
    for i in result:
        print(i,end=' ')
topology()
        