message = "The price of the current stock is:"
print(id(message))
value = "$1110"
message = message + " is" + value
print(id(message))
#We receive different id's which shows that first string wasn't changed(immutable)
print(message + " " + value)