n = int(input())
x = ['a', 'e', 'i', 'o', 'u']
results = []

for i in range(1, n+1):
    y = input()
    result = ''.join([i for i in y if i not in x])
    results.append(result)
    print(f'#{i} {result}')


