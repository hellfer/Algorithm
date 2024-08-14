t = int(input())  # 테스트 케이스 수 입력

for _ in range(t):
    original_price = float(input())  # 원래 가격 입력
    discounted_price = original_price * 0.8  # 20% 할인 적용

    # 소수점 둘째 자리까지 출력 (셋째 자리에서 반올림)
    print(f"${discounted_price:.2f}")