# write your code here
def sum_input():
    res = 0
    number = int(input("gibe number"))
    while number != 0:
        res += number
        number = int(input("gibe number"))
    res += number
    print(f"The sum equals {res}.")