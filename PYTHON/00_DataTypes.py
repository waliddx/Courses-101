# --------------------------------------------------------------------#
# DataTypes : #

# => mutable datatypes are the ones that can be modified like adding or removing somethig from it

# => immutable datatypes are the opposite you can't modify them
# --------------------------------------------------------------------#

###### mutable datatypes :

List = [1, 2, 3] # lists are ordered collections of items


dictionnaries = {
    'a': 1,
    'b': 2
} # Dictionaries are unordered collections of key-value pairs

sets = {1, 2, 3} # Sets are unordered collections of unique items


###### immutable datatypes :

integer = 5 # Integers are whole numbers without a fractional component

Float = 5.5 # Floats represent real numbers and can contain a fractional part

stringOne = "Hello" # Strings are sequences of characters

stringTwo = 'Hello' # same but with single quotes

stringThree = """hello
m walid""" # same but it helps to write a whole paragraph with new lines without \n 

Tuple = (1, 2, 3) #  Tuples are ordered collections of items, similar to lists

Frozen_Sets = frozenset({1, 2, 3}) # Frozen sets are like sets, but they are immutable and hashable, meaning they can be used as dictionary keys.



###### special type ::

my_bytes, my_bytearray = b"hello",  bytearray(b"world") #Bytes and bytearrays are used to represent sequences of bytes (integers from 0 to 255) and are immutable and mutable, respectively.

boolean = "it's either true or false" 