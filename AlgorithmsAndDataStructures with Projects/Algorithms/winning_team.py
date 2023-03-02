'''
In basketball three plays score points: a three point shot,
two point shot, and a one point free throw.We must watch and record the points
for each team.Then indicate which team is winner or the game is even.
'''

print("please enter the scores for team A")
team_a_1 = int(input())
team_a_2 = int(input())
team_a_3 = int(input())

team_a_result = team_a_1 + team_a_2 + team_a_3

print("please enter the scores for team B")
team_b_1 = int(input())
team_b_2 = int(input())
team_b_3 = int(input())

team_b_result = team_b_1 + team_b_2 + team_b_3

if(team_a_result > team_b_result):
    print("Team A wins")
if(team_b_result > team_a_result):
    print("Team B wins")
else:
    print("The game is even")
