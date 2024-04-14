import math

n=int(input())

for i in range(1,n+1):
    x=int(input())
    y=int(math.sqrt(x))
    result=float('inf')
    for j in range(y,0,-1):
        if x%j==0:
            k=x//j
            result=min(result,j-1+k-1)
            break
    print(f'#{i} {result}')
    
    
