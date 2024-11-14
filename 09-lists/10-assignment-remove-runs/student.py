def remove_runs(ns):
    lijst = list(ns)
    if len(lijst) <= 1:
        return lijst
    last_number = lijst[len(lijst) - 1]
    for i in range(len(lijst)- 2, -1, -1):
        print(lijst)
        if lijst[i] == last_number:
            lijst.pop(i)
        else:
            last_number = lijst[i]
        
    return lijst


print(remove_runs([1, 2, 2, 2, 4, 7, 9, 9, 9, 9]))
print(remove_runs([]))
print(remove_runs([1, 2]))
