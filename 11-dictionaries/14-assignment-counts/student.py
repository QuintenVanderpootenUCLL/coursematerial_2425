def counts(xs):
    result = dict()
    for el in xs:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1
    return result


print(counts(['a', 'b', 'b', 'c', 'c', 'c']))