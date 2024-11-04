team1_input = input().strip().split()
team1_1p = int(team1_input[0])
team1_2p = int(team1_input[1])
team1_3p = int(team1_input[2])

team2_input = input().strip().split()
team2_1p = int(team2_input[0])
team2_2p = int(team2_input[1])
team2_3p = int(team2_input[2])

score_team1 = team1_1p * 1 + team1_2p * 2 + team1_3p * 3
score_team2 = team2_1p * 1 + team2_2p * 2 + team2_3p * 3

if score_team1 > score_team2:
    print(1)
elif score_team2 > score_team1:
    print(2)
else:
    print(0)
