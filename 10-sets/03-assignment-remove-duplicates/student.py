def remove_duplicates(xs):
    gezien =  set()
    nieuwe_lijst = []
    for char in xs:
        if char not in gezien:
            gezien.add(char)
            nieuwe_lijst.append(char)
    return nieuwe_lijst

print(remove_duplicates([1 , 2, 5 , 5 ,6 , 7 ,8]))