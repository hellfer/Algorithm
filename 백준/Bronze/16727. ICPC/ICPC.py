p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

total_persepolis = p1 + p2
total_esteghlal = s1 + s2

if total_persepolis > total_esteghlal:
    print("Persepolis")
elif total_esteghlal > total_persepolis:
    print("Esteghlal")
else:
    away_goals_persepolis = p2  
    away_goals_esteghlal = s1 
    
    if away_goals_persepolis > away_goals_esteghlal:
        print("Persepolis")
    elif away_goals_esteghlal > away_goals_persepolis:
        print("Esteghlal")
    else:
        print("Penalty")
