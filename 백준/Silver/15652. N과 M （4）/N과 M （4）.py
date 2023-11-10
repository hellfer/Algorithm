def backtracking(n, m, result, start):
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(start, n+1):
        result.append(i)
        backtracking(n, m, result, i)
        result.pop()

n,m=map(int,input().split())
result=[]
backtracking(n, m, result, 1)