n=int(input())
result=[]
result2=[]
min=0

for _ in range(n):
    x=int(input())
    result.append(x)

y=sorted(result,reverse=True)
       
for i in range(len(y)):
    result2.append((i+1)*y[i])
    
print(max(result2))