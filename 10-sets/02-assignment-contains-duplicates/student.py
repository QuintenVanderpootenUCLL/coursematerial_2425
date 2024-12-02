def contains_duplicates(xs):
    unique_list = list(set(xs))
    return not(unique_list == xs)
