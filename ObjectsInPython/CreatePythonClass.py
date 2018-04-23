'''
The simplest possible class in Python looks like this:

class MyfirstClass:    #declaring the class
    pass               #pass is used to validate the empty class
'''

class Point:
    pass

p1 = Point()       #instance 1 of the class assigned to variable p1
p2 = Point()       #instance 2 of the class assigned to variable p2


p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)
