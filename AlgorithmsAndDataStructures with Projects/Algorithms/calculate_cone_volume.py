#the formula of calculating cone width is  (Pi * r**2 * h)/3

Pi = 3.141592653589793
print('Please enter and r value')
r = int(input())

print('Please enter an h value')
h = int(input())

result = (Pi*(r*r)*h)/3

print("The cone width is : ")
print(result)