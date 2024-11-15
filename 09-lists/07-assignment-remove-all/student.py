def remove_all(xs, item_to_remove):
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] == item_to_remove:
            xs.pop(i)
        
        
    
xs = [1] * 1000000
remove_all(xs, 1)