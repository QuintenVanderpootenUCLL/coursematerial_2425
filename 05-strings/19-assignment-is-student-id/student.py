# write your code here
def is_digit(character):
    return character in "0123456789"

def is_student_id(string):
    return (len(string) == 8) and (string[0].lower() in "rs") and is_digit(string[1]) and is_digit(string[2]) and is_digit(string[3]) and is_digit(string[4]) and is_digit(string [5]) and is_digit(string[6]) and is_digit(string[7])