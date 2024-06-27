n=int(input())
dp=[0]*101

for j in range(4,101):
    dp[0]=0
    dp[1]=1
    dp[2]=1
    dp[3]=1
    dp[j]=dp[j-3]+dp[j-2]

for i in range(1,n+1):
    x=int(input())
    print(f'#{i} {dp[x]}')

