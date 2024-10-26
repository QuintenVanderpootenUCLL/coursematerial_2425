# write your code here
def box(string):
    lengte = len(string)
    lijn = (2 + lengte) * "-"
    result = f"+{lijn}+\n| {string} |\n+{lijn}+"
    print(result)
    return (result)   

box("WEWO")
box("Put me in a box")