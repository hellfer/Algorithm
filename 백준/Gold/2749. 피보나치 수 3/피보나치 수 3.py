n=int(input())
pisano=1500000
n%=pisano
dp=[0]*(pisano+1)
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    dp[i]=(dp[i-2]+dp[i-1])%1000000
print(dp[n])
        