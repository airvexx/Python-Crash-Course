## slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

## looping through a slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())