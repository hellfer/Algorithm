T = int(input())
dp = [0] * (T + 1)
dp[1] = 1

if T > 1:
    dp[2] = 1

    for i in range(3, T + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

print(dp[T])
