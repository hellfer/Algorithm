n=int(input())
dp=[0]*(n+1)

#연산 횟수 저장, 다이나믹 프로그래밍
for i in range(2,n+1):
    dp[i]=dp[i-1]+1 #1을 빼는 연산
    
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2]+1)
    
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3]+1)
        
print(dp[n])