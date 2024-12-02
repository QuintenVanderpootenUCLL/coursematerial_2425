def inverse_lookup(dictionary, value):
    result = []
    for key, val in dictionary.items():
        if value == val:
            result.append(key)
    return result


print(inverse_lookup({'a': 1, 'b': 1, 'c': 2}, 3))
print(inverse_lookup({'a': 1, 'b': 1, 'c': 2}, 2))