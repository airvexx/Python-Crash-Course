## Airvexx
## 

guests = ['hagbard celine', 'robert anton wilson', 'israel regardie']
message_0 = "Hey, " + guests[0].title() +"!" + " Are you availible for a dinner party tonight" + "?"
message_1 = "Hey, " + guests[1].title() +"!" + " Are you availible for a dinner party tonight" + "?"
message_2 = "Hey, " + guests[2].title() +"!" + " Are you availible for a dinner party tonight" + "?"

del guests[1]

guests.insert(0, 'colin wilson')

message_0 = "Hey, " + guests[0].title() +"!" + " Are you availible for a dinner party tonight" + "?"
message_1 = "Hey, " + guests[1].title() +"!" + " Are you availible for a dinner party tonight" + "?"
message_2 = "Hey, " + guests[2].title() +"!" + " Are you availible for a dinner party tonight" + "?"

print(message_0)
print(message_1)
print(message_2)
print('Unfortunately, Robert Anton Wilson cannot make it tonight.')