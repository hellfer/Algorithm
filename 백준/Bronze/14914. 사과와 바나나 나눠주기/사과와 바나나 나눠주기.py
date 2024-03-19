n,m=map(int,input().split())

x=min(n,m)

for i in range(1,x+1):
    if n%i==0 and m%i==0:
        j=n//i
        k=m//i
        print(i,j,k)
