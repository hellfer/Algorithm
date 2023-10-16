from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a = list(map(int, input().split()))
    for i in range(1, len(a) - 1):
        graph[a[i]].append(a[i+1])
        indegree[a[i+1]] += 1
def topology():
    queue = deque()
    result = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        a = queue.popleft()
        result.append(a)
        for i in graph[a]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    if len(result) == n:
        for i in result:
            print(i)
    else:
        print(0)
topology()
