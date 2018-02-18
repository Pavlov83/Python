'''Lists are Python"s workhorse datatype,they can hold arbitrary objects and
can expand dynamically as new items are added.'''


# Creating  a list
a_list = ['myObject','Git',123,'secondObject','string',True,'another string']
print(a_list)

# As expected,lists have zero based indexes so you can print particular indexes

print(a_list[2])

''' Slicing is used to get any needed part of the list.To get any part of the
list,we need to specify two indices- beginning and end of the slice.
'''

print (a_list[0:2])

# We also can concatenate lists and the result is a new list
list = [123,'string']+['second value']
print (list)


'''if you want to add item at the end of the list you need to use the append()
function '''
a_list.append(3)
print(a_list)

''' another way of adding elements to a list is the extend() function which
accepts list as argument '''
a_list.extend(['additional element','another element'])
print(a_list)
