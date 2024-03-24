MOD=1000000007

n,m=map(int,input().split())

x=pow(m,n,MOD)
y=pow(m-1,n,MOD)
result=(x-y)%MOD

print(result)

