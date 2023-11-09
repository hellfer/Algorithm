def backtracking(N, M, result, visited):
    # 조합의 길이가 M에 도달하면 결과를 출력하고 종료
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N+1):
        # 이미 선택된 숫자는 건너뛰기
        if visited[i]:
            continue

        # 숫자 i를 선택하고 방문처리
        visited[i] = True
        result.append(i)
        
        # 다음 자리수로 이동하여 재귀 호출 
        backtracking(N, M, result, visited)
        
        # 백트래킹: 선택한 숫자를 제거하고 방문 해제
        # 함수가 종료되면 backtracking 함수를 호출한 부분으로 돌아가게 되며
        # 이때 백트래킹을 수행하여 마지막으로 추가된 숫자를 제거하고 방문 해제
        result.pop()
        visited[i] = False

N, M = map(int, input().split())

# 방문 여부를 저장하는 리스트
visited = [False] * (N+1)

# 선택된 숫자를 저장하는 리스트
result = []

# 백트래킹 함수 호출
backtracking(N, M, result, visited)
