#@ -> Dir()

# The dir() built-in function returns a sorted list of strings containing the names defined by
# a module.
# The list contains the names of all the modules, variables and functions that are defined in
# a module. Following is a simple example-
# # Import built-in module math

#code of dir() program

# import math
# content = dir(math)
# print(content)


#RELOADING A MODULE

# When a module is imported into a script, the code in the top-level portion of a module is
# executed only once.
# Therefore, if you want to reexecute the top-level code in a module, you can use
# the reload() function. The reload() function imports a previously imported module again.
# The syntax of the reload() function is this-

# reload(module_name)
#
# Here, module_name is the name of the module you want to reload and not the string
#
# containing the module name.
# For example, to reload hello module, do the following

# import math
#
# reload(math)


# should work if PYTHONPATH set module search path
# import sys
# for line in sys.path:            # here we use the sys.modules
#     print(line)


#@-> SYS MODULE

# The Python sys module provides access to any command-line arguments via
# the sys.argv. This serves two purposes-

#  sys.argv is the list of command-line arguments.
#  len(sys.argv) is the number of command-line arguments.

# Here sys.argv[0] is the program i.e. the script name.

# import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
# Now run the above script as follows −
# $ python test.py arg1 arg2 arg3