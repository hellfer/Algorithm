T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    array = [input() for _ in range(N)]
    
    # 막힌 칸의 좌표를 저장할 리스트
    result = []
    
    # 막힌 칸의 좌표를 찾아 blocked_cells에 저장
    for i in range(N):
        for j in range(N):
            if array[i][j] == '#':
                result.append((i, j))
    
    # 막힌 칸들이 하나의 정사각형을 이루는지 확인
    x1 = min(i[0] for i in result)
    y1 = max(i[0] for i in result)
    x2 = min(i[1] for i in result)
    y2 = max(i[1] for i in result)
    
    square_size = max(y1 - x1, y2 - x2) + 1
    
    if len(result) == square_size ** 2:
        print(f"#{test_case} yes")
        
    else:
        print(f"#{test_case} no")


                
