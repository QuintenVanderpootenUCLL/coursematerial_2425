def invest(amount, rate, goal):
    weeks = 0
    while amount < goal:
        amount *= rate/100 + 1
        weeks += 1
    return weeks