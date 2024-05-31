t = int(input())

for i in range(1, t+1):
    n = input()
    p='1'
    q=str(p +'/' + n + ' ') * int(n)
    print(f'#{i} {q}')
    
