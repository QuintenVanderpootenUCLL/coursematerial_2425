def rpg2(n_sides, goal):
    count_goal = 0
    count = 0
    for i in range(1, n_sides + 1):
        for n in range(1, n_sides + 1):
            if (i + n) >= goal:
                count += 1
                count_goal += 1
            else:
                count += 1
    return count_goal / n_sides**2 * 100


def rpg3(n_sides, goal):
    count_goal = 0
    count = 0
    for i in range(1, n_sides + 1):
        for n in range(1 ,n_sides + 1):
            for q in range(1 , n_sides + 1):
                if (i + n + q) >= goal:
                    count += 1
                    count_goal += 1
                else:
                    count += 1
    return count_goal / n_sides **3 * 100

print(rpg2(100, 2))
print(rpg3(5, 3))