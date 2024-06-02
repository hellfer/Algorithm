for i in range(1,11):
    n,m=input().split()
    result=[]
    for j in m:
        if len(result)==0 or result[-1] != j:
            result.append(j)
        else:
            result.pop()
    print(f"#{i} {''.join(result)}")