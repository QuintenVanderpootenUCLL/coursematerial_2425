def valid_parentheses(string):
    counter = 0
    for char in string:
        if counter < 0:
            return False
        
        if char == "(":
            counter += 1

        elif char == ")":
            counter -= 1
    if counter == 0:
        return True
    return False 


print(valid_parentheses("()()(()())"))
print(valid_parentheses(")("))
