#@  loop
# while else
# A while loop statement in Python programming language repeatedly executes a target
# statement as long as a given condition is true.

# Syntax
# The syntax of a while loop in Python programming language is
# while expression:
#     statement(s)

# Here, statement(s) may be a single statement or a block of statements with uniform
# indent. The condition may be any expression, and true is any non-zero value. The loop
# iterates while the condition is true.
# When the condition becomes false, program control passes to the line immediately
# following the loop.
# In Python, all the statements indented by the same number of character spaces after a
# programming construct are considered to be part of a single block of code. Python uses
# indentation as its method of grouping statements.

#->while loop code here.


# counter =0
# while(counter<10):
# 	print(counter)
# 	counter+=1
# else:
# 	print("good by")

# @->The Infinite Loop


# A loop becomes infinite loop if a condition never becomes FALSE. You must be cautious
# when using while loops because of the possibility that this condition never resolves to a
# FALSE value. This results in a loop that never ends. Such a loop is called an infinite loop.
# An infinite loop might be useful in client/server programming where the server needs to
# run continuously so that client programs can communicate with it as and when required.

# var = 1
# while var == 1 : # This constructs an infinite loop
#     num = int(input("Enter a number :"))
#     print ("You entered: ", num)
# print ("Good bye!")

#@ ->WHILE ELSE LOOP

# The following example illustrates the combination of an else statement with a while
# statement that prints a number as long as it is less than 5, otherwise the else statement
# gets executed.

# count = 0
# while count < 5:
#     print(count, " is less than 5")
#     count = count + 1
# else:
#     print(count, " is not less than 5")



# FOR IN LOOP

# The for statement in Python has the ability to iterate over the items of any sequence, such
# as a list or a string.

# Syntax
# for iterating_var in sequence:
#     statements(s)

# If a sequence contains an expression list, it is evaluated first. Then, the first item in the
# sequence is assigned to the iterating variable iterating_var. Next, the statements block is
# executed. Each item in the list is assigned to iterating_var, and the statement(s) block is
# executed until the entire sequence is exhausted

# for letter in 'Python':  # traversal of a string sequence
#     print('Current Letter :', letter)
# print()
# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits: # traversal of List sequence
#     print('Current fruit :', fruit)
# print("Good bye!")

#@->Using else Statement with Loops
# Python supports having an else statement associated with a loop statement.
#  If the else statement is used with a for loop, the else block is executed only if for
# loops terminates normally (and not by encountering break statement).
#  If the else statement is used with a while loop, the else statement is executed
# when the condition becomes false.

# numbers=[11,33,55,39,55,75,37,21,23,41,13]
# for num in numbers:
#     if num%2==0:
#         print('the list contains an even number')
#         break
# else:
#     print('the list doesnot contain even number')
#

#########################
#@->NESTED LOOP
# Python programming language allows the use of one loop inside another loop. The
# following section shows a few examples to illustrate the concept./

# Syntax
# for iterating_var in sequence:
#     for iterating_var in sequence:
#         statements(s)
#     statements(s)

# The syntax for a nested while loop statement in Python programming language is as
# follows
#Syntax

# while expression:
#     while expression:
#         statement(s)
#     statement(s)

# A final note on loop nesting is that you can put any type of loop inside any other type of
# loop. For example a for loop can be inside a while loop or vice versa.

#nested for lopp code here:-
# for i in range(1,11):
#     for j in range(1,11):
#         k=i*j
#         print (k, end=' ')
#     print()

# The print() function inner loop has end=' ' which appends a space instead of default
# newline. Hence, the numbers will appear in one row.
# Last print() will be executed at the end of inner for loop.



####
# for row in range(1,101):
# 	for column in range(1,11):
# 		print(row*column,end=" ")
# 	print()
###########################
# control statement

# break

# for i in "hello world":
# 	if(i=="w"):
# 		break
# 		print("good by")
# 	print(i)


# for i in "hello world":
# 	if(i=="w"):
# 		continue
# 		print("good by")
# 	print(i)


# for i in "hello world":
# 	if(i=="w"):
# 		pass
# 		break
# 	print(i)
##########################################

# Infinity Loop
# while (1 == 1):
#     print("hello")


