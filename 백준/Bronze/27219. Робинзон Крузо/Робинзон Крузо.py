n=int(input())

result=""

result+='V' * (n//5)
result+='I' * (n%5)
print(result)