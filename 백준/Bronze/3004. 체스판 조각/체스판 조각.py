def max_pieces(N):
    # 가로와 세로를 각각 (N // 2)번과 (N - N // 2)번 자르면 됩니다.
    horizontal_cuts = N // 2
    vertical_cuts = N - horizontal_cuts
    # 최대 조각 수는 (가로 자른 횟수 + 1) * (세로 자른 횟수 + 1)
    max_pieces = (horizontal_cuts + 1) * (vertical_cuts + 1)
    return max_pieces

# 입력 받기
N = int(input().strip())
# 최대 조각 수 출력하기
print(max_pieces(N))
