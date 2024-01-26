def Rev(n):
    return int(str(n)[::-1])

n,m=map(int,input().split())
print(Rev(Rev(n)+Rev(m)))