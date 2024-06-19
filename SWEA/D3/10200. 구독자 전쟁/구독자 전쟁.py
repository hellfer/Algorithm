t=int(input())

for i in range(1,t+1):
    x=list(map(int,input().split()))
    y=x[1] + x[2]
    if y >= x[0]:
        print(f'#{i} {min(x)} {y-x[0]}')
    else:
        print(f'#{i} {min(x)} 0')
        