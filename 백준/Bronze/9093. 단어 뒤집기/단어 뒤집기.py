t=int(input())

for _ in range(t):
    result=[]
    x=list(input().split())
    for j in range(len(x)):
        for k in range(1,len(x[j])+1):
            result.append(x[j][-k])
        result.append(' ')
    print(''.join(result))