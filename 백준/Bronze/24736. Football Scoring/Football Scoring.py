visiting_team = list(map(int, input().strip().split()))
home_team = list(map(int, input().strip().split()))

T_v, F_v, S_v, P_v, C_v = visiting_team
visiting_score = (T_v * 6) + (F_v * 3) + (S_v * 2) + (P_v * 1) + (C_v * 2)

T_h, F_h, S_h, P_h, C_h = home_team
home_score = (T_h * 6) + (F_h * 3) + (S_h * 2) + (P_h * 1) + (C_h * 2)

print(visiting_score, home_score)
