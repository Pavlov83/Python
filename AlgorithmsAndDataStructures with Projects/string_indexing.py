#strings are zero based and their characters can be accessed by index

breaking_bad = "I am the string of breaking bad"

print(breaking_bad[0]) # gives us first index

#if we don't know the length we can use -1 to get the last element

#Slicing

breaking_bad[0:5] # gives us the characters from 0-4

#if we want from 5 to the end we use the following
breaking_bad[5:]

#If for any reason we want the whole string,we use
breaking_bad[:]

#we can provide the slice step(third argument)

print(breaking_bad[2:10:2])

 #we can reverse a string by using the following

print(breaking_bad[: : -1])