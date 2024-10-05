N = int(input())
T = list(map(int, input().split()))

total_time = sum(T) 
break_time = (N - 1) * 8 

# 총 비용 시간 계산
total_hours = total_time + break_time
days = total_hours // 24
hours = total_hours % 24 

print(days, hours)
