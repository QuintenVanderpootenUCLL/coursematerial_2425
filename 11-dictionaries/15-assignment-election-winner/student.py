def election_winner(votes):
    if votes == ():
        return None
    result = dict()
    for vote in votes:
        if vote in result:
            result[vote] += 1
        else:
            result[vote] = 1
    largest_key = max(result, key=result.get)
    return largest_key