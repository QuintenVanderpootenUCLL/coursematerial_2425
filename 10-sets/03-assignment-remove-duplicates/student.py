def remove_duplicates(xs):
    keer1 = set()
    keer2 = set()
    for i in range(len(xs)):
        element = xs[i]
        print(len(xs))
        if element in keer1:
            if element in keer2:
                xs.pop(i)
            else:
                keer2.add(element)
        else:
            keer1.add(element)
    return xs


print(remove_duplicates(list(range(1, 10000)) * 100))