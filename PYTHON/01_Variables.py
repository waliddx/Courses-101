# --------------------------------------------------------------------#
# variable : #

# => a reusable container that holds a value in it 
# => a variable that behaves as if it were the value it contains
# => you can create multiple variables in the same line
# => you concatenate by using either '+' or ',' or 'f'
# --------------------------------------------------------------------#

# variable examples

variableOne = "firts variable"

variableTwo = "second variable"

x, y = 1, 2

x = y = z = 'same value' # they have the same value now

# concatenation examples

print("this is the " + variableOne)

print("this is", variableTwo)

print(f"i got two numbers number {x} and {y}")