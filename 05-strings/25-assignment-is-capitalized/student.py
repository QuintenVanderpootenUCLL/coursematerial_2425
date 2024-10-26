# write your code here
def is_capitalized(string):
    if string == "":
        return False
    elif string[0] == string[0].upper() and string[1:] == string[1:].lower():
        return True

    else: 
        return False