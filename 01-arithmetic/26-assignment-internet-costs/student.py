# write your code here
from math import ceil
def internet_costs(duration_in_seconds, cost_per_block):
    return(cost_per_block *(ceil(duration_in_seconds /360)))

print(internet_costs(0, 0.15))
print(internet_costs(1, 0.15))
print(internet_costs(360, 0.5))