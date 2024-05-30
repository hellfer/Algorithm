for i in range(1,11):
    n=int(input())
    x=input()
    y=input()
    count=0
    for j in range(len(y)):
        if y[j:j+len(x)]==x:
            count+=1
    print(f'#{i} {count}')

          
