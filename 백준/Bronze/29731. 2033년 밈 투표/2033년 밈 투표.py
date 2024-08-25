# Rick Astley의 공약 목록
promises = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]

# 입력 받기
N = int(input())
input_promises = [input().strip() for _ in range(N)]

# 모든 공약이 기존 공약에 속하는지 확인
for promise in input_promises:
    if promise not in promises:
        print("Yes")
        break
else:
    print("No")
