# write your code here
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    amount_eggs = eggs // eggs_per_cake
    amount_flour = flour // flour_per_cake
    amount_butter = butter // butter_per_cake
    amount_sugar = sugar // sugar_per_cake
    return(min (amount_butter,amount_eggs, amount_flour, amount_sugar))