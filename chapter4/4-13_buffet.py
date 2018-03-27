# Tuple practice

menu_item = ('chicken alfredo', 'pepperoni pizza', 'chicken wings', 'calamari', 'baked potatos')
print("Today's Selections:")
for item in menu_item:
    print('-' + item.title())

menu_item = ('chicken alfredo', 'pepperoni pizza', 'chicken wings', 'artichoke', 'chicken soup')
print('\nOur menu has been updated!')
print('\nHere are the new selections:')
for item in menu_item:
    print('-' + item.title())