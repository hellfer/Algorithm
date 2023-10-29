T=int(input())

def case():
    x=[0,0,0,0,0,0,0,0]
    y=[0,0,0,0,0,0,0,0]
    count=0
    for i in range(8):
        for j in range(8):
            if array[i][j]=='O':
                x[i]+=1
                y[j]+=1
                count+=1
                if x[i]>=2 or y[j]>=2:
                    return False
    if count==8:
        return True
    else:
        return False
for i in range(1,T+1):
    array=[list(input().strip()) for _ in range(8)]
    if case():
        print(f'#{i} yes')
    else:
        print(f'#{i} no')
