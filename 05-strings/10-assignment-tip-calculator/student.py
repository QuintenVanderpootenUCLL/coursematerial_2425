# write your code here
def tip_calculator():
    prijs = input("hoeveel kost het knappe man:")
    tip = input("hoeveel tip je jonge heer:")
    if tip == "":
        tip = 20
    res = round(int(prijs) * (float(tip)/100 + 1))
    print("You have to pay " + str(res))