'''tuple is an immutable list(this is beneficial if the code tries to alter some values)
tuple looks like a list except
it is defined by parentheses instead of square brackets'''

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

for i in dimensions:
     print(i)
     
dimensions = (400,100)

for i in dimensions:
    print(i)

menu = ('food one', 'food two','food three','food four','food five')

menu_2 =('food one_changed','food two','food three','food four','food_five changed')

for i in menu_2:
    print(i)
