def combine(d1, d2):
    new_d3 = dict()
    for key, value in d1.items():
        if value in d2:
            new_d3[key] = d2[value]
    return new_d3



d1 = {
        'cat': 'kat',
        'dog': 'hond',
        'elephant': 'olifant'
 }


d2 = {
        'kat': 'chat',
        'hond': 'chien',
        'zeehond': 'phoque'
}

print(combine(d1, d2))