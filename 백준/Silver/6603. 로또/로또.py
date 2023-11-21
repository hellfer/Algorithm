# 재귀 함수 정의
def solve(start, depth):
    # depth가 6이 되면 (즉, 6개의 로또 번호를 선택하면) 그 선택된 번호들을 출력
    if depth == 6:
        for i in range(6):
            print(number[i], end=' ')
        print()
        return
    # start부터 시작하여 로또 번호 리스트의 모든 번호에 대해 수행
    for i in range(start, len(lotto)):
        # 현재 depth의 로또 번호를 선택
        number[depth] = lotto[i]
        # 다음 depth의 값을 결정하기 위해 solve 함수를 재귀적으로 호출
        solve(i + 1, depth + 1)

# 선택된 로또 번호들을 저장할 리스트
number = [0 for _ in range(13)]

# 무한 루프
while True:
    # 사용자로부터 로또 번호를 입력받음
    lotto = list(map(int, input().split()))
    # 첫 번째 숫자가 0이면 루프를 종료
    if lotto[0] == 0:
        break
    # 첫 번째 숫자(로또 번호의 개수)를 삭제
    del lotto[0]
    # 로또 번호를 선택하는 solve 함수를 호출
    solve(0, 0)
    # 한 줄 띄우기
    print()
