result=[]
for _ in range(5):
    x=int(input())
    result.append(x)
result.sort()    
print(sum(result)//len(result))
print(result[2])
   