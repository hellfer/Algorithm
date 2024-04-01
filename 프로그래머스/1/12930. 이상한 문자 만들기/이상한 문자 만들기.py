def solution(s):
    result=''
    for i in s.split(' '):
        x=''
        for j in range(len(i)):
            if j%2==0:
                x+=i[j].upper()
            else:
                x+=i[j].lower()
        result+=x+' '
    return result[:-1]

        
        
