N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# K를 0-based index로 변환
K -= 1

for _ in range(M):
    i = int(input())
    
    if i > 0:  # 양의 정수 i
        if K < i:
            K = i - K - 1  # 배열의 처음 i개를 뒤집음
    else:  # 음의 정수 -i
        i = -i  # i를 양수로 변환
        if K >= N - i:
            K = N - (K - (N - i)) - 1  # 배열의 마지막 i개를 뒤집음

# K를 1-based index로 변환하여 출력
print(K + 1)