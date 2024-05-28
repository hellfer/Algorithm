import itertools

t = int(input())

for i in range(1, t+1):
    count=0
    result=[]
    x=list(map(int,input().split()))
    y=list(itertools.permutations(x,3))
    for j in y:
        result.append(sum(j))
    z=sorted(set(result),reverse=True)
    print(f'#{i} {z[4]}')

