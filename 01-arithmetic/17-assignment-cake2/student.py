# write your code here
def cake2(eggs, flour):
    amount_eggs = (eggs // 5)
    amount_flour = (flour // 250)
    return(min(amount_eggs, amount_flour))