## Airvexx
## Remove a guest from the list and replace with a new one.

guests = ['hagbard celine', 'robert anton wilson', 'israel regardie', 'aleister crowley', 'lao tzu', 'carl sagan']
message_0 = "Hey, " + guests[0].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_1 = "Hey, " + guests[1].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_2 = "Hey, " + guests[2].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_3 = "Hey, " + guests[3].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_4 = "Hey, " + guests[4].title() +"!" + " Are you availible for dinner party tonight" + "?"
message_5 = "Hey, " + guests[5].title() +"!" + " Are you availible for dinner party tonight" + "?"

print(message_0)
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(guests)
#####
guests = ['hagbard celine', 'robert anton wilson', 'israel regardie', 'aleister crowley', 'lao tzu', 'carl sagan']
message_0 = "Hello, " + guests[0].title() + "! " + "Are you still avaibile for dinner tonight " + "?"
message_1 = "Hello, " + guests[1].title() + "! " + "Are you still avaibile for dinner tonight " + "?"
message_2 = "Hello, " + guests[2].title() + "! " + "Are you still avaibile for dinner tonight " + "?"
message_3 = "Hello, " + guests[3].title() + "! " + "Are you still avaibile for dinner tonight " + "?"
message_4 = "Hello, " + guests[4].title() + "! " + "Are you still avaibile for dinner tonight " + "?"
message_5 = "Hello, " + guests[5].title() + "! " + "Are you still avaibile for dinner tonight " + "?"

del guests[2]
print(guests)

guests.insert(2, 'frank herbert')
print(guests)

guests = ['hagbard celine', 'robert anton wilson', 'frank herbert', 'aleister crowley', 'lao tzu', 'carl sagan']
message_0 = "Hello, " + guests[0].title() + "! " + "Are you still avaibile for dinner tonight" + "?"
message_1 = "Hello, " + guests[1].title() + "! " + "Are you still avaibile for dinner tonight" + "?"
message_2 = "Hello, " + guests[2].title() + "! " + "Are you still avaibile for dinner tonight" + "?"
message_3 = "Hello, " + guests[3].title() + "! " + "Are you still avaibile for dinner tonight" + "?"
message_4 = "Hello, " + guests[4].title() + "! " + "Are you still avaibile for dinner tonight" + "?"
message_5 = "Hello, " + guests[5].title() + "! " + "Are you still avaibile for dinner tonight" + "?"

print(message_0)
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)