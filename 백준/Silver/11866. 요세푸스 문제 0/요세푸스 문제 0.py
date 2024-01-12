from collections import deque

n,m=map(int,input().split())

queue=deque(list(range(1,n+1)))
result=[]
while queue:
    for i in range(m-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
    
print('<' + ', '.join(map(str,result)) + '>')