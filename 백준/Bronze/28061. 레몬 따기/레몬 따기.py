N = int(input())  # 나무의 수 입력
lemons = list(map(int, input().split()))  # 각 나무에 자라 있는 레몬의 개수 입력

total_lemons = 0  # 보따리에 담긴 레몬의 총 개수
max_lemons = 0  # 집에 들고 갈 수 있는 레몬의 최대 개수

for i in range(N):
    if lemons[i]>max_lemons:  # 새로 채집한 레몬의 개수가 최대 개수보다 크면 최대 개수를 갱신
        max_lemons = lemons[i]
    
    if max_lemons > 0:  # 보따리에 레몬이 담겨 있을 경우, 이동할 때마다 보따리의 레몬 개수를 1씩 감소
        max_lemons -= 1

print(max_lemons)  # 집에 들고 갈 수 있는 레몬의 최대 개수 출력
