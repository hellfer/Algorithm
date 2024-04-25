n,m=map(int,input().split())
x=list(map(int,input().split()))

count=0
result=0
end=0

for i in range(n):
    while count<m and end<n:
        count+=x[end]
        end+=1
    if count==m:
        result+=1
    count-=x[i]
    
print(result)
    