# write your code here
def all_different(xs):
    for i in range(0, len(xs)):
        for h in range(0, len(xs)):
            if xs[i] == xs[h] and i != h:
                return False
            
    return True