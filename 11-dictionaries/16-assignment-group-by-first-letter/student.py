def group_by_first_letter(strings):
    result = dict()
    for name in strings:
        letter = name[0].upper()
        if letter in result:
            result[letter].append(name)
        else:
            result[letter] = [name]
    return result

print(group_by_first_letter(['Anne', 'Albert', 'aardvark', 'Boris', 'Chris']))