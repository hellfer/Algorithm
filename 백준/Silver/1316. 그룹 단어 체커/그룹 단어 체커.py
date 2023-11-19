n=int(input())
result=0
for _ in range(n):
    x=input()
    error=0
    for i in range(len(x)-1):
        if x[i] != x[i+1]:
            check=x[i+1:]
            if check.count(x[i])>0:
                error+=1
    if error == 0:
        result+=1
print(result)