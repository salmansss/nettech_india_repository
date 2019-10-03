# @Variable
''''Variables are nothing but reserved memory locations to store values. It means that when
you create a variable, you reserve some space in the memory.
Based on the data type of a variable, the interpreter allocates memory and decides what
can be stored in the reserved memory. Therefore, by assigning different data types to the
variables, you can store integers, decimals or characters in these variables.'"

"'Python variables do not need explicit declaration to reserve memory space. The declaration
happens automatically when you assign a value to a variable. The equal sign (=) is used
to assign values to variables.
The operand to the left of the = operator is the name of the variable and the operand to
the right of the = operator is the value stored in the variable'"'''

# Example of variable:
# counter = 100
# miles = 1000.0
# name = "John"
#
# print(counter)
# print(miles)
# print(name)

# @Keyword

'''The following list shows the Python keywords. These are reserved words and you cannot
use them as constants or variables or any other identifier names. All the Python keywords
contain lowercase letters only.'''
# 31 keyword of reserved words
# and,exec,not,as,finally,or,assert,for,pass,break,print,from,class,global,raise,continue,if,return,def,import,try,del,in,while,
# elif,is,with,else,lambda,yield,except.

# @statements and comments

# ->Statements

'''Instructions that a Python interpreter can execute are called statements.
 For example, a = 1 is an assignment statement. if statement, for statement, while statement etc.'''

# Multiline statement

'''Statements in Python typically end with a new line. Python, however, allows the use of
the line continuation character (\) to denote that the line should continue. 
For example'''

# total = item_one + \
#     item_two + \
#     item_three
#
# print(total)

'''The statements contained within the [], {}, or () brackets do not need to use the line
continuation character. 
For example'''

# days = {'Monday', 'Tuesday', 'Wednesday',
#  'Thursday', 'Friday'}
# print(days)

# ->Comments

'''A hash sign (#) that is not inside a string literal is the beginning of a comment. All
characters after the #, up to the end of the physical line, are part of the comment and the
Python interpreter ignores them.
Code of comment is here:'''

# print("Hello_World")

# @ ->Indentation

'''Python does not use braces({}) to indicate blocks of code for class and function definitions
or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block
must be indented the same amount. 
For example of code are here-'''

    # x,y = 10 , 2

# @Data types

# None
# numeric
# list
# tuple
# set
# string
# range
# dictionary
#
#
# @numeric
# ->int
#
# num = 5
# print(type(num))
#
# a = 5.6
# b = int(a)
# print(type(b))
#
# ->float
# num = 2.5
# print(type(num))
# b = 5
# k = float(b)
# print(k)
#
# ->complex
# num = 6+9j
# print(type(num))
# #
# b = 5
# k = 6
# c = complex(b,k)
# print(c)
#
# ->bool
# b = 5
# k = 6
# bool = b < k
# print(bool)
# type(bool)
#
#
# #here i am usually works on list,tuple,set,dictionary, string, range
#
# Sequence
# int(True)  #->  1
# int(False) #-> 0
#
# @-> list
# lst = [25,36,45,12]
# print(type(lst))
#
# -> Set
#
# s = {25,34,45}
# print(type(s))
# print(s)
#
# @->Tuple
# t = (24,34,45,67)
# print(t)
# print(type(t))
#
#
# @-> String
# str = "salman"
# st = 'a'
# print(str)
# print(type(str))
#
# @-> Range
# print(range(10))
#
# print(list(range(2,10,2)))
#
# print(type(range(10)))
#
# @-> Dictionary
# d = {'salman':'nettech','junaid':'mts'}
# print(d)
#
# print(d.keys())
#
# print(d.values())
#
#
# print(d.get('salman'))

#@Static typing and dynamic typing

# dynamic typing->
#
# Python is a dynamically typed language.
# This means that the Python interpreter does type checking only as code runs,
# and that the type of a variable is allowed to change over its lifetime.
# The following dummy examples demonstrate that Python has dynamic typing:
#
# example->
#
# if False:
# ...     1 + "two"  # This line never runs, so no TypeError is raised
# ... else:
# ...     1 + 2
# ...
# 3
#
# >>> 1 + "two"  # Now this is type checked, and a TypeError is raised
#
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
#
#
# In the first example, the branch 1 + "two" never runs so it’s never type
# checked. The second example shows that when 1 + "two" is evaluated
# it raises a TypeError since you can’t add an integer and a string in Python.
#
# Next, let’s see if variables can change type:
#
# >>> thing = "Hello"
# >>> type(thing)
# output->
# <class 'str'>
#
# >>> thing = 28.1
# >>> type(thing)
# output->
# <class 'float'>
#
# type() returns the type of an object. These examples confirm that the type
# of thing is allowed to change,
# and Python correctly infers the type as it changes.
#
#
# ->Static Typing
#
# The opposite of dynamic typing is static typing.
# Static type checks are performed without running the program.
# In most statically typed languages, for instance C and Java,
# this is done as your program is compiled.
#
# With static typing, variables generally are not allowed to change types,
# although mechanisms for casting a variable to a different type may exist.
#
# Let’s look at a quick example from a statically typed language.
# Consider the following Java snippet:
#
# example-> java
# String thing;
# thing = "Hello";


# @->Input And Output

# Input->
# 1.Fancier Output Formatting
#
# String literal->
#
# To use formatted string literals, begin a string with f or F before the
# opening quotation mark or triple quotation mark. Inside this string,
# you can write a Python expression between { and } characters that can refer
# to variables or literal values
#
# example
# year = 2016
# event = 'Referendum'
# print(f'Results of the {year} {event}')
#
# ->Output
# 'Results of the 2016 Referendum'
#
#
# ->str.format
#
#
# The str.format() method of strings requires more manual effort.
# You’ll still use { and } to mark where a variable will be substituted and can
# provide detailed formatting directives,
# but you’ll also need to provide the information to be formatted
#
# example
#
# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
# '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
#
# ' 42572654 YES votes  49.67%'
# ->str() is used the repr function to print
#
# repr() is meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax).
#
# example
#
# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)
#
# The value of x is 32.5, and y is 40000 ...
#
# ->formatting string literal
#
# Formatted string literals (also called f-strings for short) let you include
# the value of Python expressions inside a string by
# prefixing the string with f or F and writing expressions as {expression}.
#
#
# An optional format specifier can follow the expression.
# This allows greater control over how the value is formatted.
# The following example rounds pi to three places after the decimal:
#
# example
#
# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')
# output
# The value of pi is approximately 3.142.
#
# notes:
# Passing an integer after the ':' will cause that field to be a
# minimum number of characters wide. This is useful for making columns line up.
#
#
# Other modifiers can be used to convert the value before it is formatted.
# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
#
#
# example
#
# animals = 'eels'
# print(f'My hovercraft is full of {animals}.')
# output->
# My hovercraft is full of eels.
# print(f'My hovercraft is full of {animals!r}.')
# output->
# My hovercraft is full of 'eels'.
#
#
# ->The String format() Method
# Basic usage of the str.format() method looks like this:
#
# example->
# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# output->
# We are the knights who say "Ni!"
#
#
# The brackets and characters within them (called format fields) are
# replaced with the objects passed into the str.format() method.
# A number in the brackets can be used to refer to the position of the
# object passed into the str.format() method.
#
# example->
#
# print('{0} and {1}'.format('spam', 'eggs'))
# output->
# spam and eggs
# print('{1} and {0}'.format('spam', 'eggs'))
# output->
# eggs and spam
#
# If keyword arguments are used in the str.format() method,
# their values are referred to by using the name of the argument.
#
# example->
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
#
# output->
# This spam is absolutely horrible.
#
#
# This could also be done by passing the table as keyword arguments
# with the ‘**’ notation.
#
# example->
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# output->
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
#
# This is particularly useful in combination with the built-in function vars(),
# which returns a dictionary containing all local variables.
#
# As an example, the following lines produce a tidily-aligned set of columns
# giving integers and their squares and cubes:
#
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


#@ -> Types of Operators are
# there are seven types of operator are
# Arithmetic Operators
#  Comparison (Relational) Operators
#  Assignment Operators
#  Logical Operators
#  Bitwise Operators
#  Membership Operators
#  Identity Operators


# arithmetic Operator
# a = 10
# b = 20
# print(f"add of {a} and {b} is {a+b}")
# print(f"sub of {a} and {b} is {a-b}")
# print(f"div of {a} and {b} is {a/b}")
# print(f"mul of {a} and {b} is {a*b}")
# print(f"modulo of {a} and {b} is {a%b}")
# print(f"raised of {a} and {b} is {a**b}")

# a = 5
# b = -2
# print(a//b)
# if one operand is -ve then o/p
# will be floored(lower limit)
##################################
# The following logical operators are supported by Python language. Assume variable a holds
# True and variable b holds False then
#logical Operator
# a = 2
# b = 0
# c = 3
# d = a and b and c
# d = a or b and c
# d = a and b or c
# print(d)

# a = None #False
# b = 0 #False
# d = a or "Not Initialize"
# e = b or "value is zero"
# print(d,e)
##########################
# These operators compare the values on either side of them and decide the relation among
# them. They are also called Relational operators. give the operation output as True or False

# Comparison (relational operator)
# a = 2
# b = 30
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
##########################
# Bitwise operator works on bits and performs bit-by-bit operation
# Bitwise operator
# a = 10
# b = 3
# print(a&b)
# print(a|b)
# print(b>>1)
# print(b<<1)
# print(bin(a))
##########################
#Assignment
	#--> Simple
	#--> Compound
#Simple
a = 5
# print(a)
# #compound
# a+=5
# a*=5
# a/=5
# a%=5
# a**=5
# a//=5


# print(a)
#######################
# MemberShip
# Python’s membership operators test for membership in a sequence, such as strings, lists,
# or tuples. There are two membership operators as explained below
# a = "hello world"
# print("w" in a)
# print("world" in a)
# print("World" not in a)
# b = [1,2,3,4,5]
# print(2 in b)
# print(a in a)
# a = [[1,2],3,4,5]
# b = [1,2]
# print(b in a)
#########################
# Identity Operator
# Identity operators compare the memory locations of two objects. There are two Identity
# operators as explained below
# x = 5
# print(type(x) is int)
# print(type(x) is not float)
# y = 3.23
# print(type(y) is float)
# print(type(y) is int)







