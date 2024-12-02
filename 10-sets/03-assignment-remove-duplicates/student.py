def remove_duplicates(xs):
    gezien  = set()
    unique_list = []
    for char in xs:
        if char not in gezien:
            unique_list.append(char)
            gezien.add(char)
    return unique_list
