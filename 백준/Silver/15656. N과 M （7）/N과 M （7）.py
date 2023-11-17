def backtracking(n, m, result):
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(len(x)):
        result.append(x[i])
        backtracking(n, m, result)
        result.pop()
        
n,m=map(int,input().split())
x=list(map(int,input().split()))
x=sorted(x)
result=[]
backtracking(n, m, result)