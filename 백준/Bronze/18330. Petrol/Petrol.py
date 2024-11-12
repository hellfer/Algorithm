def calculate_petrol_cost(n, k):
    total_quota = k + 60

    if n <= total_quota:
        cost = n * 1500
    else:
        within_quota = total_quota
        excess_usage = n - total_quota
        cost = (within_quota * 1500) + (excess_usage * 3000)
    
    return cost

n = int(input().strip())
k = int(input().strip())

cost = calculate_petrol_cost(n, k)

print(cost)
