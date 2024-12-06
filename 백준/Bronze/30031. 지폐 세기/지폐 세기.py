money_dict = {
    136: 1000,  # 천 원권
    142: 5000,  # 오천 원권
    148: 10000, # 만 원권
    154: 50000  # 오만 원권
}

# 입력 받기
N = int(input())

total_amount = 0  # 총액 초기화

for _ in range(N):
    width, height = map(int, input().split())
    total_amount += money_dict[width]

print(total_amount)
