#Enter calculation
#5 * 6 = 30

# Store user input of 2 numbers and the operator
num1, operator, num2 = input('Enter calculation').split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
    
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))    
    
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print("Use either + - * or /")
