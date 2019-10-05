#@-> Dictionary Defining

# Dictionary in Python
# Python dictionary is yet another unordered collection of elements.
# The difference between Python dictionary and other unordered Python data types such as
# sets lies in the fact that unlike sets,
# a dictionary contains keys and values rather than just elements.
#
# Like lists, Python dictionaries can also be changed and modified,
# but unlike Python lists the values in dictionaries are accessed using keys and not
# by their positions. All the keys in a dictionary are mapped to their respective values.
# The value can be of any data type in Python.
#
#
# Create a Dictionary in Python
# While creating a dictionary in Python, there are some rules that we need to keep
# in mind as follows:
#
# The keys are separated from their respective values by a colon (:) between them,
# and each key–value pair is separated using commas (,).
# All items are enclosed in curly braces.
# While the values in dictionaries may repeat, the keys are always unique.
# The value can be of any data type, but the keys should be of immutable data type,
# that is, (Python Strings, Python Numbers, Python Tuples).
# Here is a few Python dictionary examples:
#
# dict1 ={“Brand”:”gucci”,”Industry”:”fashion”,”year”:1921}
# print (dict1)
#
#
# Output:
# {‘Brand’: ‘gucci’, ‘Industry’: ‘fashion’, ‘year’: 1921}
#
#
#
#
# @-> Access Items in Dictionary in Python
# As discussed above, to access elements in a dictionary,
# we have to use keys instead of indexes. Now,
# there are two different ways of using keys to access elements as shown below:
#
# Using the key inside square brackets like we used to use the index inside square brackets.
# Example:
#
# dict1 = {“Brand”:”gucci”,”Industry”:”fashion”,”year”:1921}
# print(dict1[‘year’])
#
#
# Output:
# 1921
#
#
#
#
#
#
# @-> Deleting the METHOD Dictionary:
# As we have already seen, we can use the del keyword to delete a particular item by passing the key of that particular item, but that is not all we can do using the del keyword. We can also delete a whole dictionary at once using the del keyword as shown in the example below:
#
# cubes = {1:1, 2:8, 3:21, 4:64, 5:125}
# cubes.del()
# print(cubes)
#
#
# Output:
# Traceback (most recent call last):
# File “”, line 1, in
# NameError: name ‘cubes’ is not defined
#
#
#
#
#@-> Common Python Dictionary Methods
# Let’s understand some common dictionary methods by going through the following table:
#
# Method	Description
# clear()	It removes all elements from a dictionary.
# copy()	It returns a copy of a dictionary.
# fromkeys()	It returns a dictionary with the specified keys and values.
# get()	       It returns the value of a specified key.
# items()	It returns a list containing a tuple for each key–value pair.
# keys()	It returns a list containing the dictionary’s keys.
# pop()	    It removes an element with a specified key.
# popitem()	It removes the last inserted (key, value) pair.
# setdefault()	It returns the value of a specified key.
# update()	It updates a dictionary with the specified key–value pairs.
# values()	It returns a list of all values in a dictionary.
#
#
#
#
# Python Dictionary Comprehension
# Dictionary comprehension is an elegant and concise way to create new dictionary from
# an iterable in Python.
#
# Dictionary comprehension consists of an expression pair (key: value) followed
# by for statement inside curly braces {}.
#
# Here is an example to make a dictionary with each item being a pair of a number and
# its square.
#
# squares = {x: x * x for x in range(6)}
#
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(squares)
#
#
# A dictionary comprehension can optionally contain more for or if statements.
#
# An optional if statement can filter out items to form the new dictionary.
#
# Here are some examples to make dictionary with only odd items.
#
# odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
#
# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# print(odd_squares)
#

# https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593