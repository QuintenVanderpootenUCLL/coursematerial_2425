def compact(xs):
    lijst = list(xs)
    for i in range(len(lijst) -1, -1, -1):
        if lijst[i] == None:
            lijst.pop(i)
    return lijst


def compact_in_place(xs):
    for i in range(len(xs) -1, -1, -1):
        if xs[i] == None:
            xs.pop(i)