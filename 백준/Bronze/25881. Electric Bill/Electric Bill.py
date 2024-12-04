# 입력을 받기
first_rate, additional_rate = map(int, input().split())
n = int(input())

# 결과를 저장할 리스트
results = []

# 각 고객의 에너지 소비량에 대해 요금을 계산
for _ in range(n):
    consumption = int(input())
    if consumption <= 1000:
        charge = consumption * first_rate
    else:
        charge = (1000 * first_rate) + ((consumption - 1000) * additional_rate)
    
    # 결과를 리스트에 저장
    results.append(f"{consumption} {charge}")

# 결과 출력
for result in results:
    print(result)
