x=input()
y=input()
count=0
result=0

while len(x)-count>=len(y):
    if x[count:count+len(y)]==y:
        result+=1
        count+=len(y)
    else:
        count+=1
        
print(result)

