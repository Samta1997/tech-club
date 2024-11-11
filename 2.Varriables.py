#1. What will happen if you run the following code?
# x = int("world")
# y = "Hello"
# print(x + y)





#2. Identify the variable in the following code, and state its type:
# greeting = "Good Morning"
# print(type(greeting))

'''This indicates that greeting is an object of the str class, which provides various
 methods and properties associated with strings, such as .upper(), .lower(), .replace(), etc.'''





#3.What will happen if you assign the value 42 to a variable and later assign a string to the same variable?
# x = 42
# x = "Now a string"
# print(x)

'''In Python, variables are dynamic, meaning their types can change during runtime. 
Initially, x is an integer, but when assigned "Now a string", it becomes a string. 
This is allowed in Python because it's dynamically typed.'''





#4. What is the difference between global and local variables in Python? 
#Answer: Global variables are defined outside of functions and are accessible throughout the program.

# count = 10  
# def update_count():
#     global count
#     count = count + 1  
#     print(count)

# update_count()

'''The error occurs because Python treats count as a local variable due to 
the assignment count = count + 1 inside the function, but the variable count 
is also being referenced before it is assigned a value in the local scope. 
The fix would be to use the global keyword.'''





#5. Explain the concept of variable shadowing. What happens in the following code and why?

# x = 5

# def my_function():
#     # global x;
#     x = 10
#     print(x)

# my_function()
# print(x)

'''Variable shadowing occurs when a local variable has the same name as a global variable.
In the function my_function(), the local variable x shadows the global variable x.'''




#6.  What is the difference between mutable and immutable variables in Python? 
#Give an example of each and explain what happens when you modify them.'''

'''Mutable objects can be changed after they are created, while immutable objects cannot be changed.'''
# lst = [1, 2, 3]  
# lst[0] = 10
# print(lst)  

# greeting = "Hello"  
# greeting[0] = "h"  




#7.  What is the difference between is and == when comparing variables in Python? Provide an example that highlights their behavior.
''' == compares the values of two variables, while is compares their identities 
(i.e., whether they reference the same object in memory).'''
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b) 
# print(a is b)  





#8.What happens when you assign one list to another variable and modify it? Explain with an example and a solution to avoid this behavior.
'''When you assign a list to another variable, both variables point to the same object in memory, so changes to one affect the other.'''

# a = [1, 2, 3]
# b = a
# b[0] = 10
# print(a)  

#To avoid this, use the copy() method to create a shallow copy or the deepcopy() function for a deep copy:
# import copy
# a = [1, 2, 3]
# b = copy.deepcopy(a)
# b[0] = 10
# print(a) 


#9. Why does the following code raise an error, and how can you fix it?
# def outer():
#     x = 10
#     def inner():
#         nonlocal x;
#         x = x + 1  
#         print(x)
#     inner()

# outer()

''' This code raises an UnboundLocalError because the inner function tries to modify the local variable x without declaring it
as nonlocal or global. Python assumes x is a local variable in inner(), but it is being used before it is assigned a value.'''





