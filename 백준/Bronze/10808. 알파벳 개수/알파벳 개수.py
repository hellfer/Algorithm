n=input()
x=[0]*26

for i in n:
    y=ord(i)-ord('a')
    x[y]+=1

for i in x:
    print(i,end=' ')