# --------------------------------------------------------------------#
# functions :
#
# => A function is a block of code which only runs when it is called.

# => You can pass data, known as parameters, into a function.

# => A function can return data as a result.
# --------------------------------------------------------------------#

# Function Definition

def my_function():
    print("Hello from a function")

# Function Call

my_function()

# --------------------------------------------------------------------#

# Arguments

def my_function(fname):

    print(f"Hello {fname}")

my_function("Emil")

my_function("Tobias")

my_function("Linus")

# --------------------------------------------------------------------#

# Parameters or Arguments?

# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# --------------------------------------------------------------------#

# Number of Arguments

def my_function(fname, lname):

    print(f"{fname} {lname}")

my_function("Emil", "Refsnes")

# --------------------------------------------------------------------#

# Arbitrary Arguments, *args

def my_function(*kids):

    print(f"The youngest child is {kids[2]}")

my_function("Emil", "Tobias", "Linus")

# --------------------------------------------------------------------#

# Keyword Arguments

def my_function(child3, child2, child1):

    print(f"The youngest child is {child3}")

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# --------------------------------------------------------------------#

# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):

    print(f"His last name is {kid['lname']}")

my_function(fname = "Tobias", lname = "Refsnes")

# --------------------------------------------------------------------#

# Default Parameter Value

def my_function(country = "Norway"):

    print(f"I am from {country}")

my_function("Sweden")


# --------------------------------------------------------------------#

# Passing a List as an Argument

def my_function(food):

    for x in food:

        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# --------------------------------------------------------------------#

# Return Values

def my_function(x):
    
        return 5 * x

print(my_function(3))

# --------------------------------------------------------------------#

# The pass Statement

def myfunction():

    pass

# --------------------------------------------------------------------#

# Recursion

def tri_recursion(k):

    if k > 0:

        result = k + tri_recursion(k - 1)

        print(result)

    else:

        result = 0

    return result

print("\n\nRecursion Example Results")

tri_recursion(6)

# --------------------------------------------------------------------#

# Lambda

x = lambda a : a + 10

print(x(5))

# --------------------------------------------------------------------#

# Lambda

x = lambda a, b : a * b

print(x(5, 6))

# --------------------------------------------------------------------#

# Lambda

x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

# --------------------------------------------------------------------#

# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):

    return lambda a : a * n


mydoubler = myfunc(2)

mytripler = myfunc(3)