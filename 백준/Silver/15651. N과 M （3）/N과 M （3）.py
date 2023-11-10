def backtracking(n, m, result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        result.append(i)      
        backtracking(n, m, result)     
        result.pop()
        
n, m = map(int, input().split())
result = []
backtracking(n, m, result)