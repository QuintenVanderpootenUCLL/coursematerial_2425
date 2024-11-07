# write your code here
def domino_chain(dominos):
    if dominos == ():
        return True
    last_domino = dominos[0]
    for i in range(1, len(dominos)):
        if dominos[i][0] != last_domino[1]:
            return False
        last_domino = dominos[i]
    return True
print(domino_chain(((1, 2), (2, 5), (5, 3), (3, 3), (3, 0))))

         