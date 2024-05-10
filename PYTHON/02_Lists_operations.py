# --------------------------------------------------------------------#
# Lists : #

# => lists are ordered collections of items and they are mutable
# --------------------------------------------------------------------#

##### example of lists :

# list of integers :

list_of_integers = [1, 2, 3, 4, 5] # a list of integers

# list of strings :

list_of_strings = ["hello", "world"]   # a list of strings

# list of mixed datatypes :

list_of_mixed_datatypes = [1, "hello", 3.4] # a list of integers, strings and floats

# list of lists :

list_of_lists = [[1, 2, 3], [4, 5, 6]] # a list of lists called nested lists

# list of tuples :

list_of_tuples = [(1, 2), (3, 4)] # a list of tuples   

# list of dictionaries :

list_of_dictionaries = [{"a": 1, "b": 2}, {"c": 3, "d": 4}] # a list of dictionaries

# list of sets :

list_of_sets = [{1, 2}, {3, 4}] # a list of sets

# --------------------------------------------------------------------#

###### there are so many list methods that you can use to manipulate lists like :


# append() : to add an item to the end of the list

list_of_integers.append(6) # [1, 2, 3, 4, 5, 6]

# clear() : to remove all items from the list

list_of_integers.clear() # []

# copy() : to return a shallow copy of the list

list_copy = list_of_integers.copy() # [1, 2, 3, 4, 5]

# count() : to return the number of times a specified value appears in the list

list_of_integers.count(1) # 1

# extend() : to add the elements of a list (or any iterable) to the end of the current list

list_of_integers.extend([6, 7, 8]) # [1, 2, 3, 4, 5, 6, 7, 8]

# index() : to return the index of the first element with the specified value

list_of_integers.index(1) # 0

# insert() : to add an item at a specified position

list_of_integers.insert(0, 0) # [0, 1, 2, 3, 4, 5]

# pop() : to remove the item at the specified position

list_of_integers.pop(0) # [1, 2, 3, 4, 5]

# remove() : to remove the first item with the specified value

list_of_integers.remove(1) # [2, 3, 4, 5]

# reverse() : to reverse the order of the list

list_of_integers.reverse() # [5, 4, 3, 2]

# sort() : to sort the list

list_of_integers.sort() # [2, 3, 4, 5]

# --------------------------------------------------------------------#

######  built-in functions that you can use with lists :


# you can also use the built-in function len() to get the length of the list

len(list_of_integers) # 4

# you can also use the built-in function sum() to get the sum of the list

sum(list_of_integers) # 14

# you can also use the built-in function max() to get the maximum value of the list

max(list_of_integers) # 5

# you can also use the built-in function min() to get the minimum value of the list

min(list_of_integers) # 2

# you can also use the built-in function sorted() to get a new sorted list

sorted(list_of_integers) # [2, 3, 4, 5]

# you can also use the built-in function any() to return True if any item in the list is True

any(list_of_integers) # True

# you can also use the built-in function all() to return True if all items in the list are True

all(list_of_integers) # True

# you can also use the built-in function enumerate() to get an enumerate object

enumerate(list_of_integers) # <enumerate object at 0x7f8b1c1b3f00>

# you can also use the built-in function filter() to get a filter object

filter(lambda x: x > 3, list_of_integers) # <filter object at 0x7f8b1c1b3f00>