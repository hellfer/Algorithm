T = int(input())

for _ in range(T):
    n, m = input().split()
    n = int(n)
    result=[] 
    for i in m: 
        result.append(i * n) 
    
    print(''.join(result))
