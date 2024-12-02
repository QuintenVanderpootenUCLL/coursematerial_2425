def sell2(stock, model, size):
    if model in stock:
        if size in stock[model]:
            stock[model][size] -= 1
        else:
            return False
    else:
        return False
    if stock[model][size] == 0:
        del stock[model][size]
    if stock[model] == dict():
        del stock[model]
    return True
        
stock = {
                'New Balance 530': {44: 1, 45: 3, 47: 1},
                'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
                'Air Jordan 1 Retro': {46: 1},
                'Nike Air Max Tuned 1': {44: 2, 45: 1},
                'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
                'Vans Classic Slip-on Checkered': {43: 1},
            }


print(sell2(stock,'New Balance 530',44))