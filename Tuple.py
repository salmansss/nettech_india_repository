# @ ->DEFINING TUPLE
#
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
# The main difference between the tuples and the lists is that the tuples cannot be changed
# unlike lists. Tuples use parentheses, whereas lists use square brackets.
# Creating a tuple is as simple as putting different comma-separated values. Optionally, you
# can put these comma-separated values between parentheses also.

#@-> CREATING TUPLE

tup1 = ();



#@ ->Accessing Values in Tuples

# To access values in tuple, use the square brackets for slicing along with the index or indices
# to obtain the value available at that index. For example-

# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7 )
# print ("tup1[0]: ", tup1[0])
# print ("tup2[1:5]: ", tup2[1:5])




#@-> TUPLE METHOD FUNCTION USED IN TUPLE
# Function with Description
# 1 cmp(tuple1, tuple2)
# No longer available in Python 3.
# 2 len(tuple)
# Gives the total length of the tuple.
# 3 max(tuple)
# Returns item from the tuple with max value.
# 4 min(tuple)
# Returns item from the tuple with min value.
# 5 tuple(seq)
# Converts a list into tuple.
#
# @-> LIST VS TUPLE

# ---->list
# list has square bracket
# mutable
# list = [5,4.0,'a']
#  access values from list
# ordered sequence
# value can be change dynamically
# adding values in list possiable
# removing value in list possiable
#
# ---->tuple
# immutable
# tuple has parenthese
# tuple = (5,4.0,'a')
#  access values from tuple
# ordered sequence
# same as list but it is faster then list because it is immutable
# adding values in tuple not possiable
# removing value in tuple not possiable




#@ -> ADVANTAGE OF TUPLE

# The main difference between Python tuples and lists is that the elements of a
# tuple cannot be changed once they are assigned; whereas, the elements of a
# list can be changed.
#
# As tuples and lists are quite similar to each other, they are often used in
# similar kinds of situations. Although, a tuple in Python has a bunch of
# advantages over lists. Following are some of the main advantages:
#
# Iteration in a tuple is faster as compared to lists since tuples in Python are immutable.
# Tuples are generally used for different Python Data Types; whereas, lists are used for
# similar data types.
# Whenever, we need to make sure that the data remains unchanged and write protected,
# Python tuple is the best option.