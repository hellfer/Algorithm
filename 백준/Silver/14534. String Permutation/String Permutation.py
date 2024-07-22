from itertools import permutations

t = int(input())

for i in range(1, t+1):
    x = input()
    y = permutations(x)
    print(f'Case # {i}:')
    for j in y:
        print(''.join(j))