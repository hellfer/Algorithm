MOD = 1000000007

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

dp = [[0 for _ in range(K)] for _ in range(M+1)]
for num in nums:
    if num != 0: # 첫 자리 숫자는 0이 될 수 없음
        dp[1][num % K] += 1

for i in range(1, M):
    for j in range(K):
        for num in nums:
            dp[i+1][(j*10+num) % K] += dp[i][j]
            dp[i+1][(j*10+num) % K] %= MOD

print(dp[M][0])