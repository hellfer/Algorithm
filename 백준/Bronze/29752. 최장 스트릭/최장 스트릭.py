n=int(input())
result=[]
x=list(map(int,input().split()))
count=0
for i in x:
    if i != 0 :
        count+=1
    result.append(count)
    if i==0:
        count=0
    
print(max(result))