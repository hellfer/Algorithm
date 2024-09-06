def calculate_leaves(a, splitting_factors, pruned_branches):
    leaves = 1  # 처음에는 1개의 잎을 가진다.
    
    for level in range(a):
        splitting_factor = splitting_factors[level]
        pruned = pruned_branches[level]
        
        # 현재 나뭇잎 수에 분기 인자를 곱하고 가지치기를 한다.
        leaves = leaves * splitting_factor - pruned
        
    return leaves

# 메인 코드
while True:
    line = input().strip()
    if line == '0':
        break

    data = list(map(int, line.split()))
    a = data[0]  # 나무의 나이
    splitting_factors = []
    pruned_branches = []
    
    for i in range(a):
        splitting_factors.append(data[1 + 2*i])
        pruned_branches.append(data[2 + 2*i])
    
    result = calculate_leaves(a, splitting_factors, pruned_branches)
    print(result)
