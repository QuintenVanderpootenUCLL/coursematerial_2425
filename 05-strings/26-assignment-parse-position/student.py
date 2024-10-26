# write your code here
def parse_position_x(string):
    midden = string.find(",")
    return float(string[1 :midden])

def parse_position_y(string):
    lengte = len(string)
    midden = string.find(",")
    return float(string[(midden + 1):(lengte - 1)])


string = "(12.453, 9.120)"
print(parse_position_x(string))
print(parse_position_y(string))