t = int(input())  # 테스트 케이스의 수 입력

for i in range(1, t+1):
    count = 0
    a, b, c = map(int, input().split())  # a, b, c 입력
    x=c//a
    y=c//b
    z=max(x,y)
    print(f'#{i} {z}')
