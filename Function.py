#@ -> FUNCTION INTRODUCTION

# A function is a block of organized, reusable code that is used to perform a single, related
# action. Functions provide better modularity for your application and a high degree of code
# reusing.
# As you already know, Python gives you many built-in functions like print(), etc. but you
# can also create your own functions. These functions are called user-defined functions


#here the user defined function

# def Subtract(a, b):
# 	return(a-b)
#
# print( Subtract(10, 12) ) # prints -2
#
# print( Subtract(15, 6) ) # prints 9


#here  we defined the function and not call it
# def printme(str):
#     print(str)
#     return

#there are several types of function
# 1.>funtion with out parameter
#
# def hello_function():
#     print('Hello World, it\'s me.  Function.')
#
#
# hello_function()

# here the function with parameter
# here we defined the function and also call the function
# def printme(str):     # here def is keyword and function name is printme and in the parenthesis i have written to take input parameter
#     "this print to write string is passed for function"
#
#     print(str)
#     return
#
# printme("hello i am here to print the string here!")

# so here we are working on pass by reference and pass by value


# so here the function we have made the function pass by value
# def changeme(mylist):
#     print("the values insides the function before changing", mylist)
#
#     mylist[2] = 50
#
#     print("the values insides the function after changing", mylist)
#     return
#
#
# mylist = [10, 20, 30]
# changeme(mylist)
#
# print("values outsides the function", mylist)


# so here we have to make a function of pass by reference
#
# def changeme(mylist):
#     mylist = [1, 2, 3, 4]
#     print("the insides values", mylist)
#     return
#
#
# mylist = [10, 20, 30]
# changeme(mylist)
#
# print("the outsides values", mylist)

# function argument


# argument types
# 1.Required argument
# 2.Keyword argument
# 3.Default argument
# 4.variable-length arguments

# 1.Required Arguments


# def printme(str):
#     print(str)
#     return
#
#
# printme()

# output:TypeError: printme() missing 1 required positional argument: 'str'


# 2.Keyword Argument

# def printme(name, age):
#     print("Name:", name)
#     print("Age:", age)
#     return
#
# printme(age=50 , name="salman")

# 3.Default Argument

# def printinfo(name, age=35):
#     print("Name:", name)
#     print("Age:", age)
#     return
#
# printinfo(age = 50, name = "salman")
# printinfo(name="arman")

# 4.variable-length function

# def printme(arg1, *vartuple):
#     print("Output is:")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# printme(10)
# printme(70, 60, 50)


# Lambda function is also call the Anonynmous

# sum = lambda arg1, arg2: arg1 + arg2
#
# print("values of total :", sum(10, 20))
# print("values of total :", sum(20, 20))


# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("Insides the function:", total)
#     return total
#
#
# total = sum(10, 20)
#
# print("Outsides the function:", total)



# # global and local variable function are call in function we are explain here.
#
# total = 0  # this here the total is global variable
#
# # here we definition the function
#
# def sum(arg1, arg2):
#     total = arg1 + arg2;  # here the total is local variable
#     print("here the total is local variable:", total)
#     return total
#
# sum(10, 20)    # here we def the arg1 = 10 and arg2 = 20
#
# print("here the total is global variable:", total)

# sum = lambda a,b : a*a + b*b + 2*a*b
#
# print("The total of sum", sum(0, 2))

#@ ->Map function

# map() function returns a list of the results after applying the given function to each item of a
# given iterable (list, tuple etc.)
#
# syntax:-
#
# map(fun,iter)

# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

#https://www.geeksforgeeks.org/python-map-function/


# Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
# 	return n + n
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

#filter function



# filter() in python
# The filter() method filters the given sequence with the help of a function that tests each
# element in the sequence to be true or not.
#
# syntax:
#
# filter(function, sequence)
# Parameters:
# function: function that tests if each element of a
# sequence true or not.
# sequence: sequence which needs to be filtered, it can
# be sets, lists, tuples, or containers of any iterators.
# Retruns:
# returns an iterator that is already filtered.



# function that filters vowels
# def fun(variable):
# 	letters = ['a', 'e', 'i', 'o', 'u']
# 	if (variable in letters):
# 		return True
# 	else:
# 		return False
#
#
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
#
# # using filter function
# filtered = filter(fun, sequence)
#
# print('The filtered letters are:')
# for s in filtered:
# 	print(s)
