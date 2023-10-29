T=int(input())
for i in range(1,T+1):
    x=list(input())
    count1 = 0
    count2 = 0
    for j in range(len(x)):
        if x[j]=='o':
            count1+=1
        else:
            count2+=1
    if count1>=8 or count2<8:
        print(f'#{i} YES')
    elif count1<8:
        print(f'#{i} NO')
