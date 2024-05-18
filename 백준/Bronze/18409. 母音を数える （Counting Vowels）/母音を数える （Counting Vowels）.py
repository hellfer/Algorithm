x=int(input())
y=input()
z=['a','e','i','o','u']
count=0
for i in y:
    for j in z:
        if i==j:
            count+=1
       
print(count)