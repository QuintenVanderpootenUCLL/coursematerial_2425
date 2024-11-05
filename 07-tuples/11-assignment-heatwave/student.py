# write your code here
def check_heatwave(temperatures):
    30days = 0
    for temp in temperatures:
        if temp < 25:
            return False
        if temp >= 30


def heatwave(temperatures):
    if len(temperatures) < 5:
        return False
    
    