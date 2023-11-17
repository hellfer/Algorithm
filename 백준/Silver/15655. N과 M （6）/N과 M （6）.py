def backtracking(n, m, result, start):
    if len(result)==m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, len(x)):
        result.append(x[i])
        backtracking(n, m, result, i+1)
        result.pop()
        
n,m=map(int,input().split())
x=list(map(int,input().split()))
x=sorted(x)
result=[]
backtracking(n, m, result, 0)