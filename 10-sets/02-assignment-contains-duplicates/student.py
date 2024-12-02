def contains_duplicates(xs):
    gezien = set()
    for char in xs:
        if char in gezien:
            return True
        else:
            gezien.add(char)
    return False