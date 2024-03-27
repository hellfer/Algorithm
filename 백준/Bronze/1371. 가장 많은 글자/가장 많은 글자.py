import sys
from collections import defaultdict

# 알파벳 빈도수를 저장할 딕셔너리 생성
freq = defaultdict(int)

# 입력 받기 (EOF까지 모든 줄을 읽음)
for line in sys.stdin:
    for char in line:
        # 알파벳 소문자인 경우에만 빈도수 증가
        if 'a' <= char <= 'z':
            freq[char] += 1

# 가장 많이 나타난 알파벳의 빈도수 찾기
max_freq = max(freq.values())

# 빈도수가 가장 높은 알파벳을 알파벳 순으로 출력
for char in sorted(freq):
    if freq[char] == max_freq:
        print(char, end='')

# 출력 완료 후 줄 바꿈
print()
