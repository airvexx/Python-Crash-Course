## Airvexx
## insert & append

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

print("\nWe got a larger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'aleister crowley')
guests.append('JRR tolkein')

name = guests[0].title()
print(name + ", please come to dinner")

name = guests[1].title()
print(name + ", please come to dinner")

name = guests[2].title()
print(name + ", please come to dinner")

name = guests[3].title()
print(name + ", please come to dinner")

name = guests[4].title()
print(name + ", please come to dinner")

name = guests[5].title()
print(name + ", please come to dinner")