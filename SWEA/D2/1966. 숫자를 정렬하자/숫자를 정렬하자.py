t = int(input())
for i in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    print('#%d' % i, end=' ')
    for j in range(n) :
        print(data[j], end=' ')
    print()
