t = int(input())

for i in range(1, t+1):
    result = []
    n = int(input())
    x = list(map(int, input().split()))
    for j in x:
        if j *4 %3 ==0 and j*4//3 in x:
            result.append(j)
            x.remove(j*4//3)
    print(f'#{i} {" ".join(map(str, result))}')

            
        
            
                
