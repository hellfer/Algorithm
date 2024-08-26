def swap_ie(name):
    # 문자 변환을 위한 딕셔너리 생성
    swap_dict = {
        'i': 'e',
        'e': 'i',
        'I': 'E',
        'E': 'I'
    }
    
    # 각 문자를 변환하여 새로운 문자열 생성
    return ''.join(swap_dict.get(char, char) for char in name)

# 입력 받기
names = []
try:
    while True:
        name = input()
        names.append(name)
except EOFError:
    pass

# 변환된 이름 출력
for name in names:
    print(swap_ie(name))
