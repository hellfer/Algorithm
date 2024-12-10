def identify_typing_method(S):
    # 각 타법에 대한 문자열 정의
    typing_methods = {
        "in-out": ["fdsajkl;", "jkl;fdsa"],
        "out-in": ["asdf;lkj", ";lkjasdf"],
        "stairs": ["asdfjkl;"],
        "reverse": [";lkjfdsa"]
    }
    
    # 입력된 문자열과 비교
    for method, patterns in typing_methods.items():
        if S in patterns:
            return method
    
    # 어떤 타법에도 일치하지 않으면 "molu" 출력
    return "molu"

# 입력 받기
S = input().strip()
# 결과 출력
print(identify_typing_method(S))
