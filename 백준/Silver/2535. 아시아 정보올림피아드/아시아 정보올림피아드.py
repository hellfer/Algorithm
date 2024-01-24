import sys
from collections import defaultdict

n = int(input())
result = []

for _ in range(n):
    x, y, z = map(int,input().split())
    result.append((z,x,y))
    
result.sort(reverse=True)
winners=defaultdict(int)
answer=[]

for i,j,k in result:
    if winners[j]<2:
        winners[j]+=1
        answer.append((j,k))
    if len(answer)==3:
        break
            
for i,j in answer:
    print(i,j)

