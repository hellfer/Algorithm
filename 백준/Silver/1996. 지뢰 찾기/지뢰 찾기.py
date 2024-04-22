n = int(input())
mines = [list(input().strip()) for _ in range(n)]
answer = [[0]*n for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

# 지뢰가 있는 위치를 기준으로 주변 8방향 칸의 숫자를 증가시킵니다.
for i in range(n):
    for j in range(n):
        if mines[i][j] != '.':
            mine_power = int(mines[i][j])
            for direction in range(8):
                nx, ny = i + dx[direction], j + dy[direction]
                if 0 <= nx < n and 0 <= ny < n and mines[nx][ny] == '.':
                    answer[nx][ny] += mine_power

# 출력
for i in range(n):
    for j in range(n):
        if mines[i][j] != '.':
            print('*', end='')  # 지뢰가 있는 칸은 '*'로 표시
        else:
            if answer[i][j] >= 10:
                print('M', end='')  # 주변 지뢰 숫자의 합이 10 이상이면 'M'으로 표시
            else:
                print(answer[i][j], end='')  # 그 외의 경우 숫자를 그대로 출력
    print()
