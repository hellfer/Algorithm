from itertools import permutations

def compare(x, y):
    # 두 숫자를 이어붙였을 때 큰 순서대로 정렬
    return int(y + x) - int(x + y)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)  # 각 숫자를 3번 반복하여 비교 (1000 이하이므로)
    answer = str(int(''.join(numbers)))  # 정렬된 숫자를 이어붙여 문자열로 반환
    return answer

