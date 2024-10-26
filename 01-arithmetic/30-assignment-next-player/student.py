# write your code here
def next_player(player, player_count):
    return((1 + player) % player_count)

print(next_player(1, 5))
print(next_player(4, 10))
print(next_player(9, 10))