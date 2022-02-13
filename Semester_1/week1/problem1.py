import numpy as np

project = 'cake'
difficulty = np.random.randint(1, 5)
ingredients = ['flour', 'butter', 'sugar', 'eggs',
               'cocoa powder', 'baking powder']

print(f'There are{"" if "apples" in ingredients else " NO"} apples in the ingredients.')
print(f'There is{"" if "butter" in ingredients else " NO"} butter in the ingredients.')
print('eggs' in ingredients or 'margarine' in ingredients)  # the same can be done here
print('eggs' in ingredients and 'margarine' in ingredients, end='\n\n')  # and here :D

flour, butter, sugar, eggs, cocoa_powder, baking_powder = \
    175, 175, '100g', 2, '1ts', 0.5

ingredients_values = [flour, butter, sugar, eggs, cocoa_powder, baking_powder]
for i in range(len(ingredients)):
    print(f'The type of {ingredients[i]} variable is {type(ingredients_values[i])}.')
print()

for i in range(len(ingredients)):
    print(f'{ingredients[i]} - {ingredients_values[i]}')
