N = int(input())
bag = 0

while N >= 0 :
    if N % 5 == 0 :  # 5로 나누어 떨어지면
        bag += (N // 5)  # 5로 나눈 몫을 봉지 개수에 추가
        print(bag)
        break
    N -= 3  # 5의 배수가 될 때까지 설탕 무게에서 3을 빼줌
    bag += 1  # 3킬로그램 봉지 추가
else :
    print(-1)
