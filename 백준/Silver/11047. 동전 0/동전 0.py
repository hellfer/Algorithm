n,m=map(int,input().split())
result=[]
for _ in range(n):
    x=int(input())
    result.append(x)

result.sort(reverse=True)
count=0  
for i in result:
    if m>=i:
        count+=m//i
        m=m%i
print(count)