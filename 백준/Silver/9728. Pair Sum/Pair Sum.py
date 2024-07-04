t=int(input())

for i in range(1,t+1):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    x.sort()
    left=0
    right=n-1
    count=0
    while left<right:
        sum=x[left]+x[right]
        if sum==k:
            left+=1
            right-=1
            count+=1
        elif sum<k:
            left+=1
        else:
            right-=1
    print(f'Case #{i}: {count}')
            