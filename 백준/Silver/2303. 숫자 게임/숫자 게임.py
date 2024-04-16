n = int(input())  # 사람의 수를 입력받음
max_remainder = -1  # 가장 큰 나머지를 저장할 변수를 초기화
winner = -1  # 이긴 사람의 번호를 저장할 변수를 초기화

for i in range(1, n + 1):  # 각 사람에 대해 반복
    cards = list(map(int, input().split()))  # 각 사람이 가진 카드를 입력받음
    max_digit_sum = 0  # 각 사람의 가장 큰 일의 자리 합을 저장할 변수를 초기화
    for j in range(5):  # 5장의 카드에 대해 반복
        for k in range(j + 1, 5):  # j번째 카드와 k번째 카드를 제외한 나머지 카드에 대해 반복
            for l in range(k + 1, 5):  # j번째와 k번째 카드를 제외한 나머지 카드에 대해 반복
                digit_sum = (cards[j] + cards[k] + cards[l]) % 10  # 세 장의 카드의 합의 일의 자리 수를 구함
                max_digit_sum = max(max_digit_sum, digit_sum)  # 현재까지의 최대 일의 자리 합을 업데이트
    if max_digit_sum >= max_remainder:  # 현재까지의 최대 일의 자리 합이 지금까지의 최대 나머지보다 크거나 같다면
        max_remainder = max_digit_sum  # 최대 나머지를 업데이트
        winner = i  # 이긴 사람의 번호를 업데이트

print(winner)  # 이긴 사람의 번호를 출력
