x=input()
count1=0
count2=0
for i in range(len(x)):
    if x[i] == "B":
        count1+=1
    if x[i] == "C":
        count2+=1
print(count1//2+count2//2)
