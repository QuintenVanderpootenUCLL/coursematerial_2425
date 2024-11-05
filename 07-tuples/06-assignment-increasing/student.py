# write your code here
def increasing(ns):
    vorig_getal = -999999999999
    for i in range(0, len(ns)):
        if vorig_getal > ns[i]:
            return False
        else:
            vorig_getal = ns[i]
    return True