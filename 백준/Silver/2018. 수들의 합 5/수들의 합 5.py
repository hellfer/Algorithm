n=int(input())

start=1

end=1

result=1

count=0

while start<=n:
    if result==n:
        count+=1
        result-=start
        start+=1
    elif result<n:
        end+=1
        result+=end
    else:
        result-=start
        start+=1
        
print(count)
        