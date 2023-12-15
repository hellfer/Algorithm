n=int(input())

for _ in range(n):
    m=int(input())
    dict={}
    
    for _ in range(m):
        x,y=input().split()
        if y in dict:
            dict[y]+=1
        else:
            dict[y]=1
    result=1
    for i in dict.values():
        result*=(i+1)
    result-=1
    
    print(result)