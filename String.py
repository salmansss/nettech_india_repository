#@ -> DEFINING A STRING

# A string is a sequence of characters.
# A character is simply a symbol. For example, the English language has 26 characters.

# Computers do not deal with characters, they deal with numbers (binary).
# Even though you may see characters on your screen, internally it is stored and
# manipulated as a combination of 0's and 1's.

# This conversion of character to a number is called encoding, and the reverse process
# is decoding. ASCII and Unicode are some of the popular encoding used.

# In Python, string is a sequence of Unicode character. Unicode was introduced to
# include every character in all languages and bring uniformity in encoding.
# You can learn more about Unicode from here.

#@-> Different way of creating a String

# # all of the following are equivalent
# my_string = 'Hello'
# print(my_string)
#
# my_string = "Hello"
# print(my_string)
#
# my_string = '''Hello'''
# print(my_string)
#
# # triple quotes string can extend multiple lines
# my_string = """Hello, welcome to
#            the world of Python"""
# print(my_string)

#@ -> How to accessing character or element in string


# We can access individual characters using indexing and a range of characters using slicing.
# Index starts from 0. Trying to access a character out of index range
# will raise an IndexError. The index must be an integer.
# We can't use float or other types, this will result into TypeError.

# Python allows negative indexing for its sequences.

# The index of -1 refers to the last item, -2 to the second last item and so on.
# We can access a range of items in a string by using the slicing operator (colon).

# program code here


# str = 'programiz'
# print('str = ', str)
#
# #first character
# print('str[0] = ', str[0])
#
# #last character
# print('str[-1] = ', str[-1])
#
# #slicing 2nd to 5th character
# print('str[1:5] = ', str[1:5])
#
# #slicing 6th to 2nd last character
# print('str[5:-2] = ', str[5:-2])


#@ ->Escape Sequence
# If we want to print a text like -He said, "What's there?"- we can neither use
# single quote or double quotes. This will result into SyntaxError as the text
# itself contains both single and double quotes.

# print("He said, "What's there?"")

# SyntaxError: invalid syntax

# print('He said, "What's there?"')

# SyntaxError: invalid syntax
# One way to get around this problem is to use triple quotes. Alternatively,
# we can use escape sequences.

# An escape sequence starts with a backslash and is interpreted differently.
# If we use single quote to represent a string, all the single quotes inside the
# string must be escaped. Similar is the case with double quotes.
# Here is how it can be done to represent the above text.

#  code of here escape string


# using triple quotes
# print('''He said, "What's there?"''')

# escaping single quotes
# print('He said, "What\'s there?"')

# escaping double quotes
# print("He said, \"What's there?\"")



# Here is a list of all the escape sequence supported by Python.

# Escape Sequence in Python
# Escape Sequence	Description
# \newline	Backslash and newline ignored
# \\	Backslash
# \'	Single quote
# \"	Double quote
# \a	 ASCII Bell
#
# \b	ASCII Backspace
# \f	ASCII Formfeed
# \n	ASCII Linefeed
# \r	ASCII Carriage Return
# \t	ASCII Horizontal Tab
# \v	ASCII Vertical Tab
# \ooo	Character with octal value ooo
# \xHH	Character with hexadecimal value HH

# code
# print("This is \x61 \ngood example")
# This is a
# good example
# print(r"This is \x61 \ngood example")
# This is \x61 \ngood example


#@ -> Python Raw String

# Python raw string is created by prefixing a string literal with ‘r’ or ‘R’.
# Python raw string treats backslash (\) as a literal character.
# This is useful when we want to have a string that contains backslash and don’t want it
# to be treated as an escape character.

# Let’s say we want to create a string Hi\nHello in python.
# If we try to assign it to a normal string, the \n will be treated as a new line.

# example of code of raw string


# s = 'Hi\nHello'
# print(s)

# Let’s see how raw string helps us in treating backslash as a normal character.


# raw_s = r'Hi\nHello'
# print(raw_s)

# @ STRING FORMATTING EXPRESSION

# https://www.geeksforgeeks.org/python-format-function/