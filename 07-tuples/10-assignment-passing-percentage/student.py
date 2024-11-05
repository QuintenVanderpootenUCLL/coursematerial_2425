# write your code here
def passing_percentage(grades):
    counter = 0
    for el in grades:
        if el >= 10:
            counter += 1
    return int(counter / len(grades) * 100)

print(passing_percentage((20, 20)))
print(passing_percentage((5, 5, 5, 10)))