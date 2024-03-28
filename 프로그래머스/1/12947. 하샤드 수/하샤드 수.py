def solution(x):
    y=[int(i) for i in str(x)]
    if x%sum(y)==0:
        return True
    else:
        return False
