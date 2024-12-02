def cake(stock, recipe_ingredients):
    min = 100000000000000
    for ingredient in recipe_ingredients.keys():
        stock_v = stock.get(ingredient, None)
        recipe_v = recipe_ingredients.get(ingredient, None)
        if recipe_v != None and stock_v != None:
            aantal_porties = stock_v // recipe_v
            if min > aantal_porties:
                min = aantal_porties
        else:
            return 0
    return min


stock = {
    "sugar": 1500,
    "eggs": 20,
    "flour": 2000,
    "butter": 1000,
    "chocolate": 2500,
    "salt": 250
}

cake_ingredients = {
    "butter": 250,
    "eggs": 4,
    "flour": 250,
    "sugar": 250
}

print(cake(stock, cake_ingredients))