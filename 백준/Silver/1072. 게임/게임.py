x,y=map(int,input().split())

z=(y*100)//x

if z>=99:
    print(-1)
else:
    left,right=0,x
    result=-1
    while left<=right:
        mid=(left+right)//2
        a=((y+mid)*100)//(x+mid)
        if a>z:
            result=mid
            right=mid-1
        else:
            left=mid+1
            
    print(result)
