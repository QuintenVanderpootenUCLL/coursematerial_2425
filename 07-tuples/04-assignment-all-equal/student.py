# write your code here
def all_equal(xs):
    for i in range(1 ,len(xs)):
        if not(xs[0] == xs[i]):
            return False
    return True