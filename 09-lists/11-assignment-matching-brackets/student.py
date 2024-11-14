def matching_brackets(string):
    if len(string) == 1:
        return False
    haakjes = []
    for char in string:
        """ print(haakjes)
        print(char)
        print("_________________") """
        if char == '[' or char == '{' or char == '(':
            haakjes.insert(0, char)
        elif haakjes == []:
            return False
        elif char == ")":
            if not(haakjes[0] == '(') or haakjes == []:
                return False
            else:
                haakjes.pop(0)
        elif char == "}" or haakjes == []:
            if not(haakjes[0] == '{'):
                return False
            else:
                haakjes.pop(0)
        elif char == "]" or haakjes == []:
            if not(haakjes[0] == '['):
                return False
            else:
                haakjes.pop(0)
    return True
#print(matching_brackets('({)}'))
#print(matching_brackets('()'))
#print(matching_brackets("([{}])"))
#print(matching_brackets("("))
print(matching_brackets('())'))