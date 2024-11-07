# write your code here
def election_winner(votes):
    if votes == ():
        return None
    namen = []
    stemmen = []
    for vote in votes:
        if vote not in namen:
            namen.append(vote)
            stemmen.append(0)
        stemmen[namen.index(vote)] += 1
    return (namen[stemmen.index(max(stemmen))])

print(election_winner(('Kang', 'Kodos', 'Kang')))
print(election_winner(()))