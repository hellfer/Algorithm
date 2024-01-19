T=int(input())
for t in range(1, T+1):
    x=int(input())
    y=list(map(int,input().split()))
    count=0   
    for i in range(1,x-1):
        if max(y[i-1],y[i+1])>y[i] and min(y[i-1],y[i+1])<y[i]:
            count+=1
    print(f'#{t} {count}')
