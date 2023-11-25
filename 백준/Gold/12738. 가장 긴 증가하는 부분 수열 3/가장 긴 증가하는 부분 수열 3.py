# sys와 bisect 모듈을 가져옵니다.
import sys
import bisect

# 수열의 길이 N을 입력받습니다.
N = int(sys.stdin.readline())
# 수열을 입력받아 정수형으로 변환한 후 리스트에 저장합니다.
x = list(map(int, sys.stdin.readline().split()))

# dp 리스트를 생성하고 첫 번째 요소를 0으로 초기화합니다.
dp = [x[0]]

# 수열의 모든 요소를 순회합니다.
for i in range(N):
    # 만약 현재 값이 dp의 마지막 값보다 크다면
    if dp[-1] < x[i]:
        # 현재 값을 dp에 추가합니다.
        dp.append(x[i])
    else: 
        # 만약 현재 값이 dp의 마지막 값보다 작거나 같다면
        # 이분 탐색으로 현재 값이 dp에 들어갈 위치를 찾고, 그 위치의 값을 현재 값으로 변경합니다.
        dp[bisect.bisect_left(dp, x[i])] = x[i]

# dp의 첫 번째 요소 0을 제외한 길이를 출력합니다. 이 값이 가장 긴 증가하는 부분 수열의 길이입니다.
print(len(dp))
