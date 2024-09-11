x=input()
a=len(x)
b=0
c=0
for i in x:
    if i==":":
        b+=1
    if i=="_":
        c+=1
print(a+b+c*5)
