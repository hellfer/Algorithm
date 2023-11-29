n=int(input())
x=list(map(int,input().split()))
m=int(input())
start, end =1, max(x)

while start<=end:
    mid=(start+end)//2
    total = sum([min(i, mid) for i in x])  # 각 예산을 mid로 잘랐을 때의 총합
    if total<=m:  # 총합이 총 예산 m보다 작거나 같은 경우
        start=mid+1
    else:  # 총합이 총 예산 m보다 큰 경우
        end=mid-1

print(end)
