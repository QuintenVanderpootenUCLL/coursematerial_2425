def find_duplicates(xs):
    seen = set()
    duplicates = set()
    for el in xs:
        if el in seen:
            duplicates.add(el)
        else:
            seen.add(el)
    return list(duplicates)


print(find_duplicates([1, 2]))
print(find_duplicates([1, 2, 1, 3, 2, 1, 1]))