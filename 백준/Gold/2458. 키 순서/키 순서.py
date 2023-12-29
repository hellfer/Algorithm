n, m = map(int, input().split())  # 학생 수, 키를 비교한 횟수

graph = [[False] * (n+1) for _ in range(n+1)]  # 인접 행렬로 키 비교 정보 저장

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True  # a보다 b가 크다는 정보를 인접 행렬에 표시

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

answer = 0  # 키 순서를 알 수 있는 학생 수

for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if i != j and (graph[i][j] or graph[j][i]):
            count += 1
    if count == n - 1:
        answer += 1

print(answer)