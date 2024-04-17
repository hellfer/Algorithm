n = int(input())

for i in range(1, n+1):
    x = int(input())
    y = input()
    if x%2==0 and y[:x//2]==y[x//2:]:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')


