# 입력 받기
N = int(input())

# 하트 모양 정의
heart = [
    " @@@   @@@ ",
    "@   @ @   @",
    "@    @    @",
    "@         @",
    " @       @ ",
    "  @     @  ",
    "   @   @   ",
    "    @ @    ",
    "     @     "
]

# N번 반복하여 하트 출력
for _ in range(N):
    for line in heart:
        print(line)
