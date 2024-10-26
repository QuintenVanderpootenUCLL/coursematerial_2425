def remove_backspaces(string):
    index = 0 
    
    while index < len(string):
        if string[index] == "\b":
            if index - 1 < 0:
                string = ""
            else:
                string = string[: index] + string[index:]
                
        else:
            index += 1
    return string

print(remove_backspaces(""))
print(remove_backspaces("\b"))
print(remove_backspaces("abc"))
print(remove_backspaces("13\b2356\b\b45677\b8990\b\b0"))
print(remove_backspaces("abc\b\bxyz")) 