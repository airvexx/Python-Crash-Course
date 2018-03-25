## Airvexx
## 

guests = ['hagbard celine', 'robert anton wilson', 'israel regardie']

name = guests[0].title()
print(name + ", please come to dinner")

name = guests[1].title()
print(name + ", please come to dinner")

name = guests[2].title()
print(name + ", please come to dinner")

name =guests[1].title()
print("\nSorry, " + name + " can't make it to dinner")

del(guests[1])
guests.insert(1, 'colin wilson')

name = guests[0].title()
print("\n" + name + ", please come to dinner")

name = guests[1].title()
print(name + ", please come to dinner")

name = guests[2].title()
print(name + ", please come to dinner")