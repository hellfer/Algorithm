t=int(input())

for i in range(1,t+1):
    result=''
    n=int(input())
    x=input().split()
    m=len(x)//2
    if n%2==0:
        for j in range(m):
            result+=x[j]+' '+x[j+m]+' '
        print(f'#{i} {result}')
    else:
        for k in range(m):
            result+=x[k]+' '+x[k+m+1]+' '
        result+=x[m]
        print(f'#{i} {result}')
    
    