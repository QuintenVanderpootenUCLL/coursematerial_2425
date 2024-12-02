def rankings(participants):
    result = dict()
    ranking = 1
    for participant in participants:
        result[participant] = ranking
        ranking += 1
    return result

