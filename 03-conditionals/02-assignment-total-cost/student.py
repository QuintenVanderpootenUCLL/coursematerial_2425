# write your code here
def total_cost(amount):
    total_cost = amount
    if (amount < 100):
        total_cost += 10
    elif (amount >= 200):
        total_cost = 0.95 * total_cost
    return total_cost