n=int(input())
result=[]
for _ in range(n):
    start,end=map(int,input().split())
    result.append((start,end))
    
result.sort(key=lambda x: (x[1],x[0]))

end_time=0
count=0
for start,end in result:
    if start>=end_time:
        end_time=end
        count+=1
        
print(count)