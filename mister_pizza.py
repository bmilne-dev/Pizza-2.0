import time
food = 'pizza'

print("Welcome to Mr. Pizza 2.0!\n")

toppings = ['pepperoni', 'mushroom', 'onion', 'sausage', 'green peppers', 'anchovies', 'hot peppers', 'bacon']
print("Our toppings are:\n")
for topping in toppings:
    print(topping.title())
print("Each pizza can have 3 toppings max\n")

if food == 'pizza':
    topping_1 = input("First topping: ").lower()
    while topping_1 not in toppings and topping_1 != 'none':    
        topping_1 = input("First topping: ").lower()
    if topping_1 in toppings:
         topping_2 = input("Second topping: ").lower()
    elif topping_1 == 'none':
        pizza_type = 'cheese'
        topping_2 = 'none'
        topping_3 = 'none'
    while topping_2 not in toppings and topping_2 != 'none':
         topping_2 = input("Second topping: ").lower()
    if topping_2 in toppings:
        topping_3 = input("Third topping: ").lower()
    elif topping_2 == 'none' and topping_1 in toppings:
        pizza_type = topping_1.title()
        topping_3 = 'none'
    while topping_3 not in toppings and topping_3 != 'none':
        topping_3 = input("Third topping: ").lower()
    if topping_3 in toppings:
        pizza_type = topping_1.title() + ' , ' + topping_2.title() + ' , ' + topping_3.title()
    elif topping_3 == 'none' and topping_2 in toppings:
        pizza_type = topping_1.title() + ' and ' + topping_2.title()

print(f"Alright, give us a minute to make your {pizza_type} pizza.")
time.sleep(1.5)
print("\n\n...Cooking")
time.sleep(1)
print("\n\n...and Done!\n")
print("Enjoy your pizza!")

