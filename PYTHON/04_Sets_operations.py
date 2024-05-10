# --------------------------------------------------------------------#
# Sets :
#
# => Sets are unordered collections of unique items.
# --------------------------------------------------------------------#

# example of sets :

# set of integers :

set_of_integers = {1, 2, 3, 4, 5}  # a set of integers  

# set of strings :

set_of_strings = {"hello", "world"}  # a set of strings

# set of mixed datatypes :

set_of_mixed_datatypes = {1, "hello", 3.4}  # a set of integers, strings and floats

# set of lists :

set_of_lists = {frozenset({1, 2}), frozenset({3, 4})}  # a set of lists

# set of tuples :

set_of_tuples = {frozenset({1, 2}), frozenset({3, 4})}  # a set of tuples

# set of dictionaries :

set_of_dictionaries = {frozenset({1, 2}), frozenset({3, 4})}  # a set of dictionaries

# set of sets :

set_of_sets = {frozenset({1, 2}), frozenset({3, 4})}  # a set of sets

# --------------------------------------------------------------------#

###### there are so many set methods that you can use to manipulate sets like :

# add() : to add an item to the set

set_of_integers.add(6)  # {1, 2, 3, 4, 5, 6}

# clear() : to remove all items from the set

set_of_integers.clear()  # set()

# copy() : to return a shallow copy of the set

set_copy = set_of_integers.copy()  # {1, 2, 3, 4, 5}

# difference() : to return a set that contains the difference between two sets

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}

difference = set1.difference(set2)  # {1, 2, 3}

# difference_update() : to remove the items that exist in both sets

set1.difference_update(set2)  # {1, 2, 3}

# discard() : to remove the specified item

set1.discard(3)  # {1, 2}

# intersection() : to return a set that contains the intersection of two sets

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}

intersection = set1.intersection(set2)  # {4, 5}

# intersection_update() : to remove the items that are not present in both sets

set1.intersection_update(set2)  # {4, 5}

# isdisjoint() : to return whether two sets have a intersection or not

set1 = {1, 2, 3, 4, 5}

set2 = {6, 7, 8}

isdisjoint = set1.isdisjoint(set2)  # True

# issubset() : to return whether another set contains this set or not

set1 = {1, 2, 3}

set2 = {1, 2, 3, 4, 5}

issubset = set1.issubset(set2)  # True

# issuperset() : to return whether this set contains another set or not

set1 = {1, 2, 3, 4, 5}

set2 = {1, 2, 3}

issuperset = set1.issuperset(set2)  # True

# pop() : to remove a random item from the set

set1.pop()  # {2, 3, 4, 5}

# remove() : to remove the specified item

set1.remove(3)  # {2, 4, 5}

# symmetric_difference() : to return a set that contains all items from both sets, except items that are present in both sets

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}

symmetric_difference = set1.symmetric_difference(set2)  # {1, 2, 3, 6, 7, 8}

# symmetric_difference_update() : to remove the items that are present in both sets, and insert the items that are not present in both sets

set1.symmetric_difference_update(set2)  # {1, 2, 3, 6, 7, 8}

# union() : to return a set that contains all items from both sets, except duplicates

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)  # {1, 2, 3, 4, 5, 6, 7, 8}

# update() : to update the set with the union of this set and others

set1.update(set2)  # {1, 2, 3, 4, 5, 6, 7, 8}

# --------------------------------------------------------------------#