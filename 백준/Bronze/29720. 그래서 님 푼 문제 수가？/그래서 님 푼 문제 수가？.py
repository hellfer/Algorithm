n,m,k=map(int,input().split())

if n-(m*k)>0:
    print(n-(m*k),n-(m*k)+(m-1))
if n-(m*k)<=0:
    print(0,n-(m*k)+(m-1))
