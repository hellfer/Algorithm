x=input()
y=input()
a=0
b=0

while len(x)-a>=len(y):
    if x[a:a+len(y)]==y:
        b+=1
        a+=len(y)
    else:
        a+=1
        
print(b)
        