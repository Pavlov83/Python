''' You want to compare strings,checking to see whether two strings have the same value or checking
to see whether two strings have the same value or checking to see whether two names point to the same string object.

Solution: There are two ways of doing comparisons using 'is' or '=='.The first is a way of testing whether two variable names refer to
the same object.The second is a way of comparing the actual value for each variable. '''

#compare str1 and str2

str1 = 'Hello'
str2 = 'World'
if str1 == str2:
	print("The strings are equal") 
else:
    print("The strings are not equal")	

'''for comparison we can use '!=,<,>',when doing greater than or
 less then comparison strings are compared letter by letter.Python treats uppercase letters different
 than lowercase letters.Uppercase comes before lowercase,so Z comes before A.