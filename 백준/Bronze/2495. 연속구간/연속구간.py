for _ in range(3):
    x=input()
    count=1
    result=[]
    for i in range(len(x)-1):
        if x[i+1]==x[i]:
            count+=1
            result.append(count)
        if x[i+1]!=x[i]:
            count=1
    result.append(count)
    print(max(result))
   