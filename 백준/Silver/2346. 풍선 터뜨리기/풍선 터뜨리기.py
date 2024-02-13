from collections import deque

n=int(input())
x=list(map(int,input().split()))

queue=deque()

for i in range(len(x)):
    queue.append((x[i],i+1)) # 인덱스는 1부터 시작하므로 i+1
    
while queue:
    move, idx = queue.popleft()
    print(idx, end=' ')
    if not queue: 
        break
    if move > 0: 
        for _ in range(move-1): # 이동할 만큼 덱 회전
            queue.append(queue.popleft())
    else: 
        for _ in range(abs(move)): # 이동할 만큼 덱 회전
            queue.appendleft(queue.pop())

        