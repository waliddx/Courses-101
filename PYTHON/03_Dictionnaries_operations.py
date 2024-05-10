# --------------------------------------------------------------------#
# Dictionnaries :
#
# => Dictionaries are unordered collections of key-value pairs
# --------------------------------------------------------------------#

# example of dictionnaries:

# dictionary of integers :

dictionary_of_integers = {"a": 1, "b": 2, "c": 3}  # a dictionary of integers

# dictionary of strings :

dictionary_of_strings = {"name": "john", "age": "25"}  # a dictionary of strings

# dictionary of mixed datatypes :

dictionary_of_mixed_datatypes = {"a": 1, "b": "hello", "c": 3.4}  # a dictionary of integers, strings and floats

# dictionary of lists :

dictionary_of_lists = {"a": [1, 2, 3], "b": [4, 5, 6]}  # a dictionary of lists

# dictionary of tuples :

dictionary_of_tuples = {"a": (1, 2), "b": (3, 4)}  # a dictionary of tuples

# dictionary of dictionaries :

dictionary_of_dictionaries = {"a": {"a": 1, "b": 2}, "b": {"c": 3, "d": 4}}  # a dictionary of dictionaries are called nested dictionaries

# dictionary of sets :

dictionary_of_sets = {"a": {1, 2}, "b": {3, 4}}  # a dictionary of sets

# --------------------------------------------------------------------#

###### there are so many dictionary methods that you can use to manipulate dictionaries like :

# clear() : to remove all items from the dictionary

dictionary_of_integers.clear()  # {}

# copy() : to return a shallow copy of the dictionary

dictionary_copy = dictionary_of_integers.copy()  # {"a": 1, "b": 2, "c": 3}

# fromkeys() : to return a dictionary with the specified keys and values

keys = ["a", "b", "c"]

values = 0

new_dictionary = dict.fromkeys(keys, values)  # {"a": 0, "b": 0, "c": 0}

# get() : to return the value of the specified key

value = dictionary_of_integers.get("a")  # 1

# items() : to return a list containing a tuple for each key value pair

items = dictionary_of_integers.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# keys() :

keys = dictionary_of_integers.keys()  # dict_keys(['a', 'b', 'c'])

# pop() : to remove the item with the specified key name

dictionary_of_integers.pop("a")  # {"b": 2, "c": 3}

# popitem() : to remove the last item

dictionary_of_integers.popitem()  # {"b": 2}

# setdefault() : to return the value of the specified key. If the key does not exist: insert the key, with the specified value

value = dictionary_of_integers.setdefault("a", 1)  # 1

# update() : to update the dictionary with the specified key-value pairs

dictionary_of_integers.update({"d": 4})  # {"a": 1, "b": 2, "c": 3, "d": 4}

# values() : to return a list of all the values in the dictionary

values = dictionary_of_integers.values()  # dict_values([1, 2, 3, 4])

# --------------------------------------------------------------------#
