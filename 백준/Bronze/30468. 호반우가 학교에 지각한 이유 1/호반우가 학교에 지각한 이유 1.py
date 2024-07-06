STR, DEX, INT, LUK, N = map(int, input().split())

average_stat = (STR + DEX + INT + LUK) // 4
total_increase = 4 * N - (STR + DEX + INT + LUK)
min_blessing = max(0, total_increase)

print(min_blessing)
