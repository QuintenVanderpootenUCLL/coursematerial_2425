# write your code here
from math import ceil
def split_in_two(xs):
    middle = ceil((len(xs) / 2))
    return(xs[:middle], xs[middle:])


print(split_in_two((1, 2, 3, 4)))
print(split_in_two((1, 2, 3, 4, 5)))