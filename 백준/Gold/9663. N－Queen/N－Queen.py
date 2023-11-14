def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            if not (a[i] or b[x + i] or c[x - i + n - 1]):
                a[i] = b[x + i] = c[x - i + n - 1] = True
                dfs(x + 1)
                a[i] = b[x + i] = c[x - i + n - 1] = False

n = int(input())
a = [False] * n  # 열을 확인하는 리스트
b = [False] * (2 * n - 1)  # 대각선을 확인하는 리스트
c = [False] * (2 * n - 1)  # 역대각선을 확인하는 리스트
result = 0
dfs(0)
print(result)


