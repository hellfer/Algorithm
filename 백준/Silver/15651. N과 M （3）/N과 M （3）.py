def backtracking(n, m, visited, result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
            
        visited[i] = False
        result.append(i)
        
        backtracking(n, m, visited, result)
        
        
        result.pop()
        
n, m = map(int, input().split())
visited = [False] * (n+1)
result = []
backtracking(n, m, visited, result)