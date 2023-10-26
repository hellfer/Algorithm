import sys
input=sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    array = [True for i in range(2 * n + 1)]
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if array[i]:
            for j in range(i + i, 2 * n + 1, i):
                array[j] = False
    print(len([i for i in range(n + 1, 2 * n + 1) if array[i]]))

