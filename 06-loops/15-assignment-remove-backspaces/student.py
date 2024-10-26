def remove_backspaces(string):
    index = 0 
    
    while index < len(string):
        if string[index] == "\b":
            if index - 1 < 0:
                string = ""
            else:
                string = string[: index - 1] + string[index + 1:]
                
        else:
            index += 1
    return string

print(remove_backspaces(""))
print(remove_backspaces("\b"))
print(remove_backspaces("abc"))
print(remove_backspaces("13\b2356\b\b45677\b8990\b\b0"))
print(remove_backspaces("abc\b\bxyz")) 
print(remove_backspaces('1235\b084567899\b080'))