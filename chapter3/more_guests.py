## Airvexx
## insert & append

guests = ['hagbard celine', 'robert anton wilson', 'israel regardie']
message_0 = "Hey, " + guests[0].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_1 = "Hey, " + guests[1].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_2 = "Hey, " + guests[2].title() +"!" + " Are you availible for dinner party tonight" + "?"

del guests[1]

guests.insert(0, 'colin wilson')
guests.insert(2, 'carl sagan')
guests.append('richard feynman')

message_0 = "Hey, " + guests[0].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_1 = "Hey, " + guests[1].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_2 = "Hey, " + guests[2].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_3 = "Hey, " + guests[3].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_4 = "Hey, " + guests[4].title() +"!" + " Are you availible for dinner party tonight" + "?"


print(message_0)
print(message_1)
print(message_2)
print(message_3)
print(message_4)

print('Unfortunately, Robert Anton Wilson cannot make it tonight, but I"ve found a bigger table!')