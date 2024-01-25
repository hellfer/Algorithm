T=int(input())
result=[]
for _ in range(T):
    x=input()
    result.append(x)

result1=list(result[0])
for i in result:
    for j in range(len(result1)):
        if result1[j]!=i[j]:
            result1[j]='?'
print(''.join(result1))