t=int(input())

for i in range(1,t+1):
    result=[]
    y=list(map(int,input().split()))
    y=y[1:]
    y.sort()
    for j in range(len(y)-1):
        result.append(y[j+1]-y[j])
    print(f'Class {i}')
    print(f'Max {y[-1]}, Min {y[0]}, Largest gap {max(result)}')
        