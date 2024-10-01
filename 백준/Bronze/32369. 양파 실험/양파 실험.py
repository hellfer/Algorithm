# 입력 받기
N, A, B = map(int, input().split())

praising_onion = 1  # 칭찬 양파
blaming_onion = 1   # 비난 양파

for _ in range(N):
    praising_onion += A
    blaming_onion += B
    
    if blaming_onion > praising_onion:
        praising_onion, blaming_onion = blaming_onion, praising_onion
    elif blaming_onion == praising_onion:
        blaming_onion -= 1

print(praising_onion, blaming_onion)
