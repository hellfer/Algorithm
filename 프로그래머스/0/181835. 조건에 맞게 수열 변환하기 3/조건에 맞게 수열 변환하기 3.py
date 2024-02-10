def solution(arr, k):
    result=[]
    for i in arr:
        if k%2 == 0:
            i=i+k
            result.append(i)
        else:
            i=i*k
            result.append(i)
    return result