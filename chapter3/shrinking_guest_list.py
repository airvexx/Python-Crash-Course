## Airvexx
## delete with pop and del

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

not_invited_1 = guests.pop(2)
not_invited_2 = guests.pop(3)
not_invited_3 = guests.pop(1)

print(guests)
print('I cannot invite you tonight ' + not_invited_1.title() + '.')
print('I cannot invite you tonight ' + not_invited_2.title() + '.')
print('I cannot invite you tonight ' + not_invited_3.title() + '.')
print(guests)

print('Are you still free tonight ' + guests[0].title() + "?")
print('Are you still free tonight ' + guests[1].title() + "?")


print('Unfortunately, I can only invite two of you tonight.')

del guests[0]
del guests[-0]
print(guests)