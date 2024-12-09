# 입력 받기
test_cases = int(input())

for _ in range(test_cases):
    c, v = map(int, input().split())
    
    # 각 형제가 받을 사탕의 개수
    candies_per_brother = c // v
    # 아버지가 남길 사탕의 개수
    candies_for_dad = c % v
    
    # 결과 출력
    print(f"You get {candies_per_brother} piece(s) and your dad gets {candies_for_dad} piece(s).")
