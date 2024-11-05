# write your code here
def subtuple(xs, ys):
    if ys == ():
        return True
    if not(ys[0] in xs):
        return False
    first = xs.index(ys[0])
    for i in range(0, len(ys)):
        if not(xs[first + i] == ys[i]):
            return False
    return True

print(subtuple(('a', 'b', 'c', 'd', 'e'), ('b', 'c', 'd')))