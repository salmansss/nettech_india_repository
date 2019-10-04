#@ IF STATEMENT


# The IF statement is similar to that of other languages. The if statement contains a logical
# expression using which the data is compared and a decision is made based on the result
# of the comparison.

# syntax
#
# if expression:
#     statement(s)


# If the boolean expression evaluates to TRUE, then the block of statement(s) inside the if
# statement is executed. In Python, statements in a block are uniformly indented after the
# : symbol. If boolean expression evaluates to FALSE, then the first set of code after the
# end of block is executed

# Example CODE:

# var1 = 100
# if var1:
#     print("1 - Got a true expression value")
#     print(var1)

#@ IF__ELSE STATEMENT

# An else statement can be combined with an if statement. An else statement contains a
# block of code that executes if the conditional expression in the if statement resolves to
# 0 or a FALSE value.
# The else statement is an optional statement and there could be at the most only
# one else statement following if.

# Syntax
# The syntax of the if...else statement is

# if expression:
#     statement(s)
# else:
#     statement(s)

#code of if else example:

# amount=int(input("Enter amount: "))
# if amount<1000:
#     discount=amount*0.05
#     print("Discount",discount)
# else:
#     discount=amount*0.10
#     print("Discount",discount)
#
# print("Net payable:",amount-discount)
#


#@ IF__ELIF__ELSE :-

# The elif statement allows you to check multiple expressions for TRUE and execute a block
# of code as soon as one of the conditions evaluates to TRUE.
# Similar to the else, the elif statement is optional. However, unlike else, for which there
# can be at the most one statement, there can be an arbitrary number of elif statements
# following an if.


# Syntax
# if expression1:
#     statement(s)
# elif expression2:
#     statement(s)
# elif expression3:
#     statement(s)
# else:
#     statement(s)


# amount=int(input("Enter amount: "))
# if amount<1000:
#     discount=amount*0.05
#     print ("Discount",discount)
# elif amount<5000:
#     discount=amount*0.10
#     print ("Discount",discount)
# else:
#     discount=amount*0.15
#     print ("Discount",discount)
# print ("Net payable:",amount-discount)
#


#@ NESTED IF_ELSE

# There may be a situation when you want to check for another condition after a condition
# resolves to true. In such a situation, you can use the nested if construct.
# In a nested if construct, you can have an if...elif...else construct inside another
# if...elif...else construct.
# Syntax
# The syntax of the nested if...elif...else construct may be
# if expression1:
#     statement(s)
#     if expression2:
#         statement(s)
#     elif expression3:
#         statement(s)
#     else
#         statement(s)
# elif expression4:
#     statement(s)
# else:
#     statement(s)

# num = int(input("Enter the number:"))
# if num%2==0:
#     if num%3==0:
#         print ("Divisible by 3 and 2")
#     else:
#         print ("divisible by 2 not divisible by 3")
# else:
#     if num%3==0:
#         print ("divisible by 3 not divisible by 2")
#     else:
#         print ("not Divisible by 2 not divisible by 3")
#
