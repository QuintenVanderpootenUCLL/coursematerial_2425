# write your code here
def empty_seats(used_seats):
    empty = 0
    last = 1
    for seat in used_seats:
        if seat - last > 1:
            empty += seat - last - 1
        #print(empty)
        last = seat
    return empty  

print(empty_seats((1, 3, 5)))
print(empty_seats((1, 2, 3)))