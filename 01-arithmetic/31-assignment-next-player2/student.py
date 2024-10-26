# write your code here
def next_player2(player, player_count):
    return(player % (player_count) + 1)

print(next_player2(4, 10))
print(next_player2(10, 10))
print(next_player2(24, 25))