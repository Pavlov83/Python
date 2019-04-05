cars = ['audi','bmw','jaguar','ford']

for car in cars:

    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

    
#Conditional tests:

        car = 'bmw'
        car == 'bmw'  #returns true

        
#using if statements in multiple lists


available_toppings = ['pepperoni','mushrooms','olives']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_top in requested_toppings:
    if requested_top in available_toppings:
        print("Adding" + "Requested top")
    else:
        print("Sorry,we dont")

print("Finished your pizza")        
