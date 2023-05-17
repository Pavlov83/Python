# variables

#Variables are not objects themselves,they are pointers/references to objects

a = [2,4,6]
# a is a variable which points to a list object
b = a
'''
we are making variable b which points to the object referenced by a

if we make a change it reflects to both objects

The variables accept the type they point to.It can change dynamically
during program execution
'''

#variable scope

x = 10; y = 20

def my_function():
    global y
    x=11; y=21
my_function()
print(x)
print(y)
