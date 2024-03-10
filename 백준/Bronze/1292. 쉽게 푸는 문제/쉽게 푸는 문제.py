n,m=map(int,input().split())
x=0
result=[]

for i in range(1,m+1):
    for j in range(i):
        result.append(i)        
for i in range(n-1,m):
    x+=result[i]    
    
print(x)