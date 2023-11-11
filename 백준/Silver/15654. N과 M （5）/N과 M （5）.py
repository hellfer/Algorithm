def backtracking(n, m, result, visited):
    if len(result)==m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(len(x)):
        if visited[i]:
            continue
        visited[i]=True
        result.append(x[i])
        backtracking(n, m, result, visited)
        visited[i]=False
        result.pop()
        
n,m=map(int,input().split())
x=list(map(int, input().split()))
x=sorted(x)
visited=[False]*(n+1)
result=[]
backtracking(n, m, result, visited)