n, d = map(int, input().split())

problems_solved = []

for _ in range(n):
    problems_solved.append(int(input()))

total_problems = sum(problems_solved)

reward_per_problem = d // total_problems

for problems in problems_solved:
    reward = problems * reward_per_problem
    print(reward)
