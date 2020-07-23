number_of_balls = int(input())
team1_score = int(input())
team2_score = int(input())
balls_bowled = int(input())

overs = (number_of_balls//6 + (number_of_balls%6)/10)
overs_finished = (balls_bowled//6 + (balls_bowled%6)/10)
current_run_rate = round(team2_score/overs_finished,1)
run_rate = round(team1_score/overs , 2)

runs_to_win = team1_score+1
remaining_balls = number_of_balls - balls_bowled
remaining_runs = runs_to_win - team2_score

if(remaining_runs/remaining_balls <= 6):
    ans = "Eligible to win "

else:
    ans = "Not eligible to win"

print(overs)
print(overs_finished)
print(current_run_rate)
print(run_rate)
print(ans)
