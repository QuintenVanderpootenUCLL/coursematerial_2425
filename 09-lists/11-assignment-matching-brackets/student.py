def matching_brackets(string):
    haakjes = []
    for char in string:
        #print(char)
        #print(haakjes)
        #print("______________")
        if char == '[' or char == '{' or char == '(':
            haakjes.insert(0, char)
        elif char == ")":
            if not(haakjes[0] == '(') or haakjes == []:
                return False
            else:
                haakjes.remove("(")
        elif char == "}" or haakjes == []:
            if not(haakjes[0] == '{'):
                return False
            else:
                haakjes.remove("{")
        elif char == "]" or haakjes == []:
            if not(haakjes[0] == '['):
                return False
            else:
                haakjes.remove("[")
    return True
#print(matching_brackets('({)}'))
#print(matching_brackets('()'))
print(matching_brackets("(([]){}){([][])}"))