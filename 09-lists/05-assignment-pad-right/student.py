def pad_right(xs, length, padding):
    while len(xs) < length:
        xs.append(padding)
xs = [1, 2, 3, 4]
pad_right(xs, 6, 0)
print(xs)