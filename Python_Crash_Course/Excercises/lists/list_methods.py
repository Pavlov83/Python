names = ["Walter","Jesse","Gustavo","Mike","Saul"]

# append() adds and item to the end of the list
names.append("Hank")

print(names)

#insert() adds an item to the given index

names.insert(1,"Hector")

print(names)

#remove(x) removes the first item in the list whose value is x
names.remove("Hank")

print(names)

'''
pop([i]) sometimes we need to remove and use the index given as argument or last item 
if no argument is given
'''

popped_name = names.pop()

print(popped_name)
