n=int(input())
m=int(input())
x=input()

count=0
result=0
i=1

while i<m-1:
    if x[i-1]=='I' and x[i]=='O' and x[i+1]=='I':
        count+=1
        if count==n:
            count-=1
            result+=1
        i+=1
    else:
        count=0
    i+=1
    
print(result)
            
            