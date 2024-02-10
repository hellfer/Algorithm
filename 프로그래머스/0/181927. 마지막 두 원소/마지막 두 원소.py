def solution(num_list):
    result = []
    result.extend(num_list)
    if result[-1] > result[-2]:
        result.append(result[-1] - result[-2])
    else:
        result.append(result[-1] * 2)
    return result
