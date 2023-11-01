T = int(input())
for i in range(1, T + 1):
    N = int(input())
    count = 0  # 원점을 미리 포함시킨다.
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if x * x + y * y <= N * N:
                count += 1
    print(f'#{i} {count}')
