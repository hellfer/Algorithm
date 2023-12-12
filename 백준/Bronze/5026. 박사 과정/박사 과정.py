n = int(input())

for _ in range(n):
    x = input().split('+')
    if 'P=NP' in x:
        print('skipped')
    else:
        result = map(int, x)
        print(sum(result))
