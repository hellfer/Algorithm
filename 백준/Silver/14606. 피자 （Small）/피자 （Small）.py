def max_enjoyment(n):
    # dp[i]는 높이가 i인 피자탑에서 얻을 수 있는 최대 즐거움
    dp = [0] * (n + 1)
    
    # 높이가 1인 피자탑은 분리할 수 없으므로 0
    for h in range(2, n + 1):
        for i in range(1, h):
            # h를 i와 h-i로 분리
            dp[h] = max(dp[h], dp[i] + dp[h - i] + i * (h - i))
    
    return dp[n]

# 입력 받기
N = int(input())
result = max_enjoyment(N)
print(result)
