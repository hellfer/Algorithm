while True:
    x=int(input())
    if x==0:
        break
    result=[]
    y=list(map(int,input().split()))
    for i in range(len(y)-2):
        result.append(sum(y[i:i+3]))
    print(max(result))