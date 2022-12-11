from random import uniform, choices
def eliminate_team(teams):
    probabilities = [team/sum(teams) for team in teams]
    teams.remove(choices(teams, probabilities[::-1])[0])
    return teams
def find_quality():
    teams = sorted([uniform(0, 1) for _ in range(4)])
    teams14, teams23 = [teams[0], teams[3]], [teams[1], teams[2]]
    teams14, teams23 = [eliminate_team(team) for team in [teams14, teams23]]
    return eliminate_team(teams14+teams23)[0]
def get_answers(simulations):
    total = 0
    for _ in range(simulations):
        total += find_quality()
    print(total/simulations)
get_answers(100000)
    


                                
    
