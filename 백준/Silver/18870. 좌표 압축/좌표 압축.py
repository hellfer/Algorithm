n=int(input())
x=list(map(int,input().split()))

sorted_x=sorted(list(set(x)))

result={sorted_x[i]: i for i in range(len(sorted_x))}

for i in x:
    print(result[i], end=' ')