result=[]
for _ in range(3):
    a=int(input())
    result.append(a)

result.sort()    

if result[0]+result[1]==result[2]:
    print(1)
else:
    print(0)