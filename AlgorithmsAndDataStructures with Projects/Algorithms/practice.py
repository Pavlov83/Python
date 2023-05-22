from pprint import pprint
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#
# my_list = []
# list_size = 21
#
# for i in range(21):
#            my_list.append(str(i))
#
# print(my_list)
#
# my_list

# a = ["1",1, "1",2]
#
# a = list(set(a))
# print(a)
#
# my_dict = {"a" :1,"b": 2}
#
# print(my_dict["b"])
#
# print("result is",my_dict["a"] + my_dict["b"])
#
# d ={"a":1,"b":2,"c":3}
#
# #calculate sum of dictionary values
# print("result from d is:",d["a"] + d["b"] + d["c"])
#
# d = {"a":list(range(1,11)),"b":list(range(11,21)),"c":list(range(21,31))}
# pprint(d)
#
# print(d["b"][2])
#
#
#
# for i in range(1,10):
#     print(i)


#Acceleration calculator

# def acceleration_calc(v2,v1,t2,t1):
#     a = (v2-v1) / (t2 -t1)
#     print(a)
#
# acceleration_calc(0,10,0,20)

# r = 10
# Pi = 3.14159265
#
# def liquid_volume(Pi,r,h):
#     volume = ((4*Pi*r**3)/3) - ((Pi*h**2*(3*r - h))/3)
#     print(volume)
#
# liquid_volume(Pi,r,2)

# def count_words(string):
#     string_list = string.split()
#     return len(string_list)
#
# print(count_words("Hey Ho Let's go"))
#
# def words_amount(filepath):
#     with open(filepath) as f:
#         content = f.read()
#         words = content.split()
#         return len(words)
#
# print(words_amount('words1.txt'))

# a = [1,2,3]
# b = [3,4,5]
# 1
# for i,j in zip(a,b):
#     print(i + j)

# import string
#
# with open("letters.txt","w") as file:
#     for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
#         file.write(letter1 + letter2 + "\n")


# Guessing game
import random

def guessing_game():
    number = random.randint(0,100)
    input_number = int(input("please enter a number \n"))

    if(number == input_number):
        print("the number is: ",number)
    elif(number > input_number):
        print("the number is too low")
    else:
        print("number is too high")

guessing_game()