def make_teams(participants, team_size):
    teams = []
    current = 0
    while current + team_size <= len(participants):
        teams.append(participants[current:current + team_size])
        current += team_size
    if teams == []:
        teams = [[]]
    for i in range(0, len(participants) - current):
        teams[i].append(participants[current + i])
    return teams

#print(make_teams(['Annie', 'Ashley', 'Butcher', 'Frenchie', 'Hughie', 'John', 'Kimiko', 'Maeve'], 4))
#print(make_teams(['Annie', 'Ashley', 'Butcher', 'Frenchie', 'Hughie', 'John', 'Kimiko', 'Maeve'], 3))
print(make_teams(["a"], 2))