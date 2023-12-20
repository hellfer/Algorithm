n, m = map(int, input().split())
x = list(map(int, input().split(',')))

result=[]

for _ in range(m):
    result = []
    for i in range(0,len(x)-1):
        result.append(x[i + 1] - x[i])
    x=result

y = ','.join(map(str,x))
print(y)

