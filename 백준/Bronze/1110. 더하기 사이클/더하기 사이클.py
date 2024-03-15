n = int(input())
count = 0
result=n
while True:
    x = n // 10
    y = n % 10
    z = (y * 10) + ((x + y) % 10)
    count += 1

    if z == result:
        break
        
    n=z

print(count)
