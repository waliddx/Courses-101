# --------------------------------------------------------------------#
# Loops :
#
# => With the while loop we can execute a set of statements as long as a condition is true.

# => With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# --------------------------------------------------------------------#

# while loop

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# Example

# Print i as long as i is less than 6:

i = 1

while i < 6:

    print(i)

    i += 1

# Note: remember to increment i, or else the loop will continue forever.

# for loop

# The for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Example

# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]

for x in fruits:

    print(x)

# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String

# Even strings are iterable objects, they contain a sequence of characters:

# Example

# Loop through the letters in the word "banana":

for x in "banana":

    print(x)

# The break Statement

# With the break statement we can stop the loop before it has looped through all the items:

# Example

# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]

for x in fruits:

    print(x)

    if x == "banana":

        break

# The continue Statement

# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# Example

# Do not print banana:

fruits = ["apple", "banana", "cherry"]

for x in fruits:

    if x == "banana":

        continue

    print(x)

# The range() Function

# To loop through a set of code a specified number of times, we can use the range() function,

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Example

# Using the range() function:

for x in range(6):

    print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

# Example

# Using the start parameter:

for x in range(2, 6):

    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

# Example

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):

    print(x)

# Else in For Loop

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Example

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):

    print(x)

else:

    print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Nested Loops

# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Example

# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]

fruits = ["apple", "banana", "cherry"]

for x in adj:

    for y in fruits:

        print(x, y)

# The pass Statement

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# Example

# for loop with no content:

for x in [0, 1, 2]:

    pass

# --------------------------------------------------------------------#

# Looping Through a Dictionary

# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Example

# Print all key names in the dictionary, one by one:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x in thisdict:

    print(x)

# Example

# Print all values in the dictionary, one by one:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x in thisdict:

    print(thisdict[x])

# You can also use the values() function to return values of a dictionary:

# Example

# Print all values in the dictionary, one by one:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x in thisdict.values():

    print(x)

# You can use the keys() function to return the keys of a dictionary:

# Example

# Print all key names in the dictionary, one by one:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x in thisdict.keys():

    print(x)

# Example

# Loop through both keys and values, by using the items() function:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x, y in thisdict.items():

    print(x, y)

# --------------------------------------------------------------------#