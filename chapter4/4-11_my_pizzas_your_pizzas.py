my_pizza = ['pepperoni', 'salami', 'cheese']
friend_pizza = my_pizza[:]

my_pizza.append('sausage')
friend_pizza.append('olive')

print("My favorite pizzas are:")
for pizza in my_pizza:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
    print("- " + pizza)