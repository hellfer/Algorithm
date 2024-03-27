from collections import Counter
import string

lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

text = ''.join(lines)  # 입력된 모든 줄을 하나의 문자열로 합침
text = text.replace(' ', '')  # 문자열에서 공백을 제거

# 알파벳 소문자만 있는지 확인
if all(c in string.ascii_lowercase for c in text):
    # 가장 많이 나온 글자를 찾음
    counter = Counter(text)
    max_count = max(counter.values())
    most_common = [char for char, count in counter.items() if count == max_count]
    most_common.sort()  # 알파벳 순으로 정렬
    print(''.join(most_common))  # 결과 출력
else:
    print("입력에 알파벳 소문자 이외의 문자가 포함되어 있습니다.")
