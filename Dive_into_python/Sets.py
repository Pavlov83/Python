#Sets are unordered containers of unique values.On sets you can do operations
#like union,intersection and difference.Sets are using curly brackets.

my_set = {1,2}

my_set.add(3) #adds the value of 3 at the end of the set

my_set.update({4,5,6})

#prints {1,2,3,4,5,6}


# union() method returns a new set containing all the elements that are in either set
#intersection() returns contains new seth with the elements that are in both sets
#difference returns new set with all the elements that are in a_set but not in b_set
#symmetric_difference returns a new set containing all the elements that are in
#exactly one of the sets


'''We can remove values from a set by remove(),pop() and discard()
   discard() method takes a single value as an argument and removes it
   if there is no such value, there is no error.

   The remove() uses the same concept except if there is no such value-
   we have an KeyError exception
    When using the pop() method,since the lists are unordered - there is no way to
    control which value was removed.
