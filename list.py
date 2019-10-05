# LIST IS MUTABLE MEAN IN THIS WE CAN INSERT UPDATE AT A RUNTIME

# @ -> DEFINING A LIST

# list is a built-in function and it an array in it we can do several operation we
# can perform in it
# Lists are mutable sequences, typically used to store collections of homogeneous items
# (where the precise degree of similarity will vary by application).

#@ -> creating a list

# class list([iterable])
# Lists may be created in several ways:
#
# Using a pair of square brackets to denote the empty list: []
#
# Using square brackets, separating items with commas: [a], [a, b, c]
#
# Using a list comprehension: [x for x in iterable]
#
# Using the type constructor: list() or list(iterable)

#@ -> Acessing a list

# The list data type has some more methods. Here are all of the methods of list objects:
#
# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
#
# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
#
# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#
# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
#
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
#
# list.clear()
# Remove all items from the list. Equivalent to del a[:].
#
# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
#
# list.count(x)
# Return the number of times x appears in the list.
#
# list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#
# list.reverse()
# Reverse the elements of the list in place.
#
# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].
#

# An example that uses most of the list methods:
# >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# >>> fruits.count('apple')
# 2
# >>> fruits.count('tangerine')
# 0
# >>> fruits.index('banana')
# 3
# >>> fruits.index('banana', 4)  # Find next banana starting a position 4
# 6
# >>> fruits.reverse()
# >>> fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# >>> fruits.append('grape')
# >>> fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# >>> fruits.sort()
# >>> fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# >>> fruits.pop()
# 'pear'

#


#@ -> DELETING A LIST

# remove() Parameters
# The remove() method takes a single element as an argument and removes it from the list.
#
# If the element(argument) passed to the remove() method doesn't exist, valueError
# exception is thrown.
#
# Return Value from remove()
# The remove() method only removes the given element from the list.
# It doesn't return any value.
# code here of delete a list


# animal list
# animal = ['cat', 'dog', 'rabbit', 'guinea pig']
#
# 'rabbit' element is removed
# animal.remove('rabbit')
#
# Updated Animal List
# print('Updated animal list: ', animal)
#
#@ -> IMPLEMENTATION of STACK AND QUEUE USING PYTHON
# The list methods make it very easy to use a list as a stack, where the last element
# added is the first element retrieved (“last-in, first-out”). To add an item to the
# top of the stack, use append(). To retrieve an item from the top of the stack, use pop()
# without an explicit index. For example:
#
# >>> stack = [3, 4, 5]
# >>> stack.append(6)
# >>> stack.append(7)
# >>> stack
# [3, 4, 5, 6, 7]
# >>> stack.pop()
# 7
# >>> stack
# [3, 4, 5, 6]
# >>> stack.pop()
# 6
# >>> stack.pop()
# 5
# >>> stack
# [3, 4]


# @Using LIST as QUEUE

# It is also possible to use a list as a queue, where the first element added
# is the first element retrieved (“first-in, first-out”); however, lists are not
# efficient for this purpose. While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow
# (because all of the other elements have to be shifted by one).
#
# To implement a queue, use collections.deque which was designed to have fast
# appends and pops from both ends. For example:
#
# >>> from collections import deque
# >>> queue = deque(["Eric", "John", "Michael"])
# >>> queue.append("Terry")           # Terry arrives
# >>> queue.append("Graham")          # Graham arrives
# >>> queue.popleft()                 # The first to arrive now leaves
# 'Eric'
# >>> queue.popleft()                 # The second to arrive now leaves
# 'John'
# >>> queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])



#@->  List Comprehensions



# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is the result of
# some operations applied to each member of another sequence or iterable,
# or to create a subsequence of those elements that satisfy a certain condition.
#
# For example, assume we want to create a list of squares, like:
#
# >>> squares = []
# >>> for x in range(10):
# ...     squares.append(x**2)
# ...
# >>> squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Note that this creates (or overwrites) a variable named x that still exists
# after the loop completes. We can calculate the list of squares without any side
# effects using:
#
# squares = list(map(lambda x: x**2, range(10)))
#
#
# or, equivalently:
#
# squares = [x**2 for x in range(10)]
# which is more concise and readable.
#
# A list comprehension consists of brackets containing an expression followed by a
# for clause, then zero or more for or if clauses. The result will be a new list
# resulting from evaluating the expression in the context of the for and if clauses
# which follow it. For example, this listcomp combines the elements of two lists if
# they are not equal:
#
# >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


#@-> FUNCTION IS USED IN LIST


# The following Python functions can be used on lists.
#
# Method	Description	Examples
# len(s)
# Returns the number of items in the list.
#
# The len() function can be used on any sequence
# (such as a string, bytes, tuple, list, or range) or collection
# (such as a dictionary, set, or frozen set).

# a = ["bee", "moth", "ant"]
# print(len(a))
# RESULT
# 3

# list([iterable])
# The list() constructor returns a mutable sequence list of elements.
# The iterable argument is optional. You can provide any sequence or collection
# (such as a string, list, tuple, set, dictionary, etc).
# If no argument is supplied, an empty list is returned.

# Strictly speaking, list([iterable]) is actually a mutable sequence type.
#
# print(list())
# print(list([]))
# print(list(["bee", "moth", "ant"]))
# print(list([["bee", "moth"], ["ant"]]))

# ​
# a = "bee"
# print(list(a))
# ​

# a = ("I", "am", "a", "tuple")
# print(list(a))
# ​

# a = {"I", "am", "a", "set"}
# print(list(a))
# RESULT
# []
# []


# ['bee', 'moth', 'ant']
# [['bee', 'moth'], ['ant']]
# ['b', 'e', 'e']
# ['I', 'am', 'a', 'tuple']
# ['am', 'I', 'a', 'set']
# max(iterable, *[, key, default])

#
# or

#
# max(arg1, arg2, *args[, key])
#
# Returns the largest item in an iterable (eg, list) or the largest of two or more
# arguments.
#
# The key argument specifies a one-argument ordering function like that used for sort().
#
# The default argument specifies an object to return if the provided iterable is empty.
# If the iterable is empty and default is not provided, a ValueError is raised.
#
# If more than one item shares the maximum value, only the first one encountered is
# returned.
#
# a = ["bee", "moth", "ant"]
# print(max(a))
# ​
# a = ["bee", "moth", "wasp"]
# print(max(a))
# ​
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4]
# print(max(a, b))

# RESULT

# moth
# wasp
# [1, 2, 3, 4, 5]
# min(iterable, *[, key, default])
#
# or
#
# min(arg1, arg2, *args[, key])
#
# Returns the smallest item in an iterable (eg, list) or the smallest of two or more
# arguments.
#
# The key argument specifies a one-argument ordering function like that used for sort().
#
# The default argument specifies an object to return if the provided iterable is empty.
# If the iterable is empty and default is not provided, a ValueError is raised.
#
# If more than one item shares the minimum value, only the first one encountered is
# returned.
#
# a = ["bee", "moth", "wasp"]
# print(min(a))
# ​
# a = ["bee", "moth", "ant"]
# print(min(a))
# ​
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4]
# print(min(a, b))
# RESULT
# bee
# ant
# [1, 2, 3, 4]
# range(stop)
#
# or
#
# range(start, stop[, step])
#
# Represents an immutable sequence of numbers and is commonly used for looping a
# specific number of times in for loops.
#
# It can be used along with list() to return a list of items between a given range.
#
# Strictly speaking, range() is actually a mutable sequence type.
#
# print(list(range(10)))
# print(list(range(1,11)))
# print(list(range(51,56)))
# print(list(range(1,11,2)))
# RESULT
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [51, 52, 53, 54, 55]
# [1, 3, 5, 7, 9]

#@ -> USING ZIP() IN LIST

# zip() in conjunction with the * operator can be used to unzip a list:
#
# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y)
# list(zipped)
# OUTPUT HERE->
# [(1, 4), (2, 5), (3, 6)]


#@ -> MATRIX OPERATION USING LIST


# In Python, we can implement a matrix as nested list (list inside a list).
# We can treat each element as a row of the matrix.
#
# For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix.
# First row can be selected as X[0] and the element in first row,
# first column can be selected as X[0][0].
#
# We can perform matrix addition in various ways in Python. Here are a couple of them.
#
# Source code: Matrix Addition



# Program to add two matrices using nested loop

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# iterate through rows
# for i in range(len(X)):
#    iterate through columns
   # for j in range(len(X[0])):
   #     result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)