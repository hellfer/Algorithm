n=int(input())
x=list(map(int,input().split()))
x.sort()
result=0

for i in range(n):
    for j in range(i+1):
        result+=x[j]
        
print(result)