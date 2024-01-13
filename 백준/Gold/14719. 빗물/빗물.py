H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 각 위치에서 왼쪽으로의 최대 높이를 저장하는 리스트
left_max = [0] * W
left_max[0] = blocks[0]
for i in range(1, W):
    left_max[i] = max(left_max[i-1], blocks[i])

# 각 위치에서 오른쪽으로의 최대 높이를 저장하는 리스트
right_max = [0] * W
right_max[-1] = blocks[-1]
for i in range(W-2, -1, -1):
    right_max[i] = max(right_max[i+1], blocks[i])

water = 0
for i in range(W):
    water += min(left_max[i], right_max[i]) - blocks[i]

print(water)
