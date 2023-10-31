T = int(input()) #테스트케이스 수 입력
count = [(1, 0), (0, 1)] + [0] * 40 #0이 출력되는 횟수와 1이 출력되는 횟수를 저장

for i in range(2, 41):
    count[i] = (count[i-1][0] + count[i-2][0], count[i-1][1] + count[i-2][1])

for _ in range(T):
    n = int(input())
    print(*count[n]) #count[1]은 (3, 4)라는 튜플을 반환, 튜플의 각 요소가 언패킹되어 3 4가 출력



