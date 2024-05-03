count=0
while True:
    try:
        x=input()
        count+=1
    except EOFError:
        break
        
print(count)
    