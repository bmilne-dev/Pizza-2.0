# Pizza toppings: Write a loop that prompts the user to enter a series 
# of pizza toppings until they enter a 'quit' value. As they enter each
# topping, print a message saying you'll add that topping to their pizza.
   
greeting = "Hi, welcome to Pizza Land! What can I get for you?"
size_choice = "Medium, Large, or Extra Large: "
size_list = ['medium', 'large', 'extra large', 'xl'] 
confirm_options = ['yes', 'no', 'y', 'n']
active = True

while active == True:
    print(greeting)
    size = input(size_choice)
    while size not in size_list:
        print("Sorry, I didn't recogize that size")
        size = input(size_choice.lower())
if size = 'xl':
    size.upper()
else:
    size.title()

    print("\nAlright, now for the toppings!")
    topping_list = []
    question = "What topping would you like? "
    question += "\n(Enter 'none' for cheese and 'quit' when you're finished)"
    question += "\nTopping: "

    while True:
        topping = input(question).lower()
        if topping != 'quit' and topping != 'none':
            topping_list.append(topping)
        if topping == 'quit' and len(topping_list) == 0:
            print("Alright, I get it. No pizza for you.")
            active = False
        elif topping == 'none':
            break
        elif topping == 'quit' and len(topping_list) >= 1:
            break

    if topping == 'none':
        print(f"So you want a {size} Cheese pizza?")
        a = input("Yes/No: ").lower()
        while a not in confirm_options:      # this is not working.
            print("Sorry, I didn't understand your input")
            a = input("Yes/No: ").lower()
        if a == 'yes':
            print(f"\nAlright! your pizza is in the oven!")
            active = False
        else:
            print("Alright, would you like to start over?")
            a = input("Yes/No: ").lower()
            while a not in confirm_options:      # this is not working.
                print("Sorry, I didn't understand your input")
                a = input("Yes/No: ").lower()
            if a == 'yes':
                print("Starting over!")
            else:
                print("Quitting!")
                active = False

    if topping == 'quit':
        print("\nAlright, so you want a pizza with the following toppings:")
        for toppings in topping_list:
            print(toppings.title())
        a = input("Yes/No: ").lower()
        while a not in confirm_options:      # this is not working.
            print("Sorry, I didn't understand your input")
            a = input("Yes/No: ").lower()
        if a == 'yes':
            print(f"\nYour pizza is in the oven!")
            active = False
        if a == 'no':
            print("Alright, would you like to start over?")
            a = input("Yes/No: ").lower()
            if a == 'no':
                active = False
