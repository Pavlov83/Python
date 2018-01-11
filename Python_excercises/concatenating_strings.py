'''If you want to build strings up from a number of smaller strings.This process is called concatenation.
 Solution: The simplest way tp build up a string is to use the + operator.In this case,the strings are put together and
the complete new string is returned. 
'''
new_str = 'hello ' + 'world'
print(new_str)

# multiplicative_concatenation

new_str = 'Hello' * 3
print(new_str)

# concatenating_non-strings

new_str = "Count = " + str(42)
print(new_str)
