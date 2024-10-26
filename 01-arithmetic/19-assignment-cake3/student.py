# write your code here
def cake3(eggs, flour, butter, sugar):
    amount_eggs = (eggs // 5)
    amount_flour = (flour // 250)
    amount_butter = (butter // 200)
    amount_sugar = (sugar // 250)
    return(min(amount_eggs, amount_butter, amount_flour, amount_sugar))