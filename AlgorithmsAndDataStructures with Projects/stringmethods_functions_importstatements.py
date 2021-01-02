#length of an object can be obtained by using len() built-in function

greeting = "Hello"
user="Pavlov"
message = "Welcome to python"
print(greeting,user,message)


len(greeting) #gives us the type of the object

type(message) #gives us the type of the object

#we can change to capital letters

user.upper()

#If there is any whitespace in the beginning or ending
# of a string we use strip()

# if we search for some element in a string we use find() which gives the index
print(message.find('to'))

#if we want to make a list from a string of strings we use split()
print(message.split()) # we can specify split character e.g. , - or so on....

# join makes the opposite ,takes list and make a string from the indexes
# the same way we can use join character , - or any other
