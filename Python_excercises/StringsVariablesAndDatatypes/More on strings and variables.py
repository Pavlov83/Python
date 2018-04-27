a = 12
b = 3
print(a + b / 3 -4 * 12)
print(8 / 2 * 3)
print(8 * 3 /2)

print(((((a + b) / 3)-4) *12))

c = a + b
d = c / 3
e = d - 4
print(e * 12)


# string mainpulation and slicing

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])    #prints w
print(parrot[-1])   #prints e
print(parrot[0:6])  #prints Norweg (from the beginning to the sixth)
print(parrot[6:])   #prints from position six to the end
print(parrot[0:6:2])#prints Nre
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])
numbers = "1,2,3,4,5,6,7,8,9"
print(numbers[0::3])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("Hello" *5)
print("Hello" *5 +"4")  #appends 4 at the end

#searching in strings

today = "friday"
print("day" in today)     #returns True if it is there



