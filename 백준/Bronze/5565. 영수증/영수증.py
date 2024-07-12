result=[]
for _ in range(10):
    x=int(input())
    result.append(x)

y=0
for j in range(1,10):
    y+=result[j]

print(result[0]-y)