# write here your code

def heatwave(temperatures):
    day25 = 0
    day30 = 0
    counter = 0
    while counter < len(temperatures):
        if day25 >= 5 and day30 >= 3:
            return True
        if temperatures[counter] >= 25:
            day25 += 1
        if temperatures[counter] >= 30:
            day30 += 1
        if temperatures[counter] < 25:
            day25 = 0
            day30 = 0
        counter += 1
    if day25 >= 5 and day30 >= 3:
            return True
    return False



print(heatwave((40, 20, 40, 40, 40, 40)))
print(heatwave((24, 26, 28, 31, 29, 27, 32, 25, 27, 26, 30, 23)))
print( heatwave([40, 40, 20, 40, 40, 40]))