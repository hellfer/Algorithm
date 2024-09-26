# 入力を受け取る
S = int(input())
A = int(input())
B = int(input())

# 基本の高さ A cm で S cm 以上にするための高さ不足を計算
height_needed = max(0, S - A)

# 追加のアイスクリームの数を計算
if height_needed > 0:
    additional_ice_creams = (height_needed + B - 1) // B  # 切り上げ計算
else:
    additional_ice_creams = 0

# コスト計算
base_cost = 250
additional_cost = additional_ice_creams * 100
total_cost = base_cost + additional_cost

# 結果を出力
print(total_cost)

