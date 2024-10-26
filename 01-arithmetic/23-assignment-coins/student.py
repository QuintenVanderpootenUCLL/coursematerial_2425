# write your code here
def coins(amount):
    amount_of_coins = 0
    amount = amount
    def calc_amount_of_coins(coin, amount):
        return(amount // coin)
    amount_of_coins += calc_amount_of_coins(5, amount)
    amount -= calc_amount_of_coins(5, amount) * 5
   
    amount_of_coins += calc_amount_of_coins(2, amount)
    amount -= calc_amount_of_coins(2, amount) * 2

    amount_of_coins += calc_amount_of_coins(1, amount)
    amount -= calc_amount_of_coins(1, amount)

    return(amount_of_coins)

    