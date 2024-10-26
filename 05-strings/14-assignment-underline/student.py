# write your code here
def underline(string):
    lengte = len(string)
    onderlijn = lengte * "-"
    result = f"{string}\n{onderlijn}"
    print(result)
    return result

underline("abc")
underline("some string")