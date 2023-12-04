n=int(input())
x=list(map(int,input().split()))
result=[]

for i in range(len(x)):
    result.append(x[i]/max(x)*100)

average=sum(result)/n    
print(average)