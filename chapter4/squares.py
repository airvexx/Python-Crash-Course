squares = []                    #verbose way
for value in range(1,11):
   square = value**2
   squares.append(square)
print(squares)

squares = []                            #a more concise way
for value in range(1,11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range (1,11)]              #an even better way
print(squares)