n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
result=0
for i in range(len(x)):
    if x[i]<y[i]:
        result+=y[i]-x[i]
        
print(result)