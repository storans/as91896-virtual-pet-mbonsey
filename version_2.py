# Create a universal integer checking function that can be used in a range of situations
def check_int(question, error, low, high):
    valid = False
    while not valid:
        # Any question that needs a number
        number = input("{}: ".format(question))
        try:
            number = int(number)
            # If the number chosen is greater than the lower value and less than the higher value, the number is returned
            if low <= number <= high:
                return number
            else:
                print(error)
                print()
        # If an invalid input is made, the prompt is given again
        except ValueError:
            # The error printed will be customised to the question
            print(error)

# Create a universal float checking function that can be used in a range of situations
def check_float(question, error, low, high):
    valid = False
    while not valid:
        # Ask any question that requires a number as the response
        number = input("{}: ".format(question))
        try:
            number = float(number)
            # If the number chosen is greater than the lower value and less than the higher value, the number is returned
            if low <= number <= high:
                return number
            else:
                print(error)
                print()
        # If an invalid input is made, the prompt is given again
        except ValueError:
            # The error printed will be customised to the question
            print(error)

# Create a dictionary of different things eg. weight and exercise, that user can check about their rabbit
MAIN_DICT = {1: "feed", 2: "exercise", 3: "check weight", 4: "end game", 5: "help"}

# Create a dictionary with each food that the user can choose from
FOOD_DICT = {1: "kale", 2: "broccoli", 3: "apple"}

# Create a dictionary with each food and the number of kilograms it will add to the weight of the rabbit
FOOD_WEIGHT_DICT = {"kale": 0.3, "broccoli": 0.2, "apple": 0.4}

# Create a dictionary with each exercise that the user can choose from
EXERCISE_DICT = {1: "hopping", 2: "running", 3: "walking"}

# Create a dictionary with each exercise and the number of kilograms it will subtract from the weight of the rabbit
EXERCISE_WEIGHT_DICT = {'hopping': 0.3, 'running': 0.5, 'walking': 0.1}

# Create a function that prints the main menu
def main_menu():
    print("Select an option from this menu! Perhaps, you want to feed your rabbit, or maybe check their weight?")
    print("     1. Feed {}".format(rabbit_name))
    print("     2. Exercise {}".format(rabbit_name))
    print("     3. Check {}'s Weight".format(rabbit_name))
    print("     4. End Game")
    print("     5. Help")
    print("     6. Restart")
    print()

    # Ask the user to input the number that relates to the action they want to perform
    main_choice = check_int("Type a number, between 1 and 6, from the list above", "This number is not between 1 and 6.", 1, 6)
    print()
    # Return the user's choice
    return main_choice

# Create a function that will be called when the user selects option 1
def feed():
    # Print a menu with the food that the user can choose from
    print("Good choice! What food would you like to feed {}?".format(rabbit_name))
    print("     1. Kale (+ 0.3kg)")
    print("     2. Broccoli (+ 0.2kg)")
    print("     3. Apple (+ 0.4kg)")
    print()

    # Ask the user to input the number that relates to the food that they want to feed their rabbit
    food_choice = check_int("Type a number, between 1 and 3, from the list above".format(rabbit_name), "This number is not between 1 and 3.", 1, 3)
    print()
    # Create a variable called food_weight that calls the number of kilograms that each food will add to the rabbit's original weight
    food_weight = FOOD_WEIGHT_DICT[FOOD_DICT[food_choice]]
    # Create a variable called new_weight that adds the number of kilograms that the selected food will add to the rabbit's weight
    new_weight = rabbit_weight + food_weight

    # Print a message that tells the user how many kilograms will be added to their rabbit's weight
    print("Yum! Since {} ate {}, we will add {}kg to your rabbit's weight.".format(rabbit_name, FOOD_DICT[food_choice], food_weight))
    print()
    # Return the rabbit's new weight
    return check_weight(new_weight)

# Create a function that will be called when the user selects option 2
def exercise():
    # Print a menu with the exercises that the use can choose from
    print("This sounds like fun! What exercise would you like {} to do?".format(rabbit_name))
    print("     1. Hopping (- 0.3kg)")
    print("     2. Running (- 0.5kg)")
    print("     3. Walking (- 0.1kg)")
    print()

    # Ask the user to input the number that relates to the exercise that they want their rabbit to do
    exercise_choice = check_int("Type a number, between 1 and 3, from the list above".format(rabbit_name), "This number is not between 1 and 3.", 1, 3)
    print()
    # Create a variable called exercise_weight that calls the number of kilograms that each exercise will remove from the rabbit's weight
    exercise_weight = EXERCISE_WEIGHT_DICT[EXERCISE_DICT[exercise_choice]]
    # Update the variable new_weight that updates the rabbit's weight by subtracting the number of kilograms that the selected exercise will remove from the rabbit's weight
    new_weight = rabbit_weight - exercise_weight

    # Print a message that tells the user how many kilograms will be removed from their rabbit's current weight
    print("{} is exhausted from that exercise! Since they did a {} exercise, we will take away {}kg from their weight.".format(rabbit_name, EXERCISE_DICT[exercise_choice], exercise_weight))
    print()
    # Return the rabbit's new weight
    return check_weight(new_weight)

# Create a function that checks the rabbit's weight
def check_weight(new_weight):
    # If the rabbit's weight is between the two valid values, the weight of the rabbit will print
    if 1.5 <= new_weight <= 2.5:
        continue_game = True
        print("{}'s weight is now {:.2f}kg!".format(rabbit_name, new_weight))
        print()
        return new_weight
    # If the rabbit's weight is not between the two valid values, an if statement will determine how the rabbit died
    else:
        # If the rabbit was under 1.5kg, they died because they were underweight
        if 1.5 > new_weight:
            print("I'm really sorry, {} but {} died because they were underweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {:.2f}kg.\nI hope you enjoyed playing Virtual Pet!".format(user_name, rabbit_name, rabbit_name, new_weight))
            print()
        # If the rabbit was over 2.5kg, they died because they were overweight
        if 2.5 < new_weight:
            print("I'm really sorry, {} but {} died because they were overweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {:.2f}kg.\nI hope you enjoyed playing Virtual Pet!".format(user_name, rabbit_name, rabbit_name, new_weight))
            print()
        # If the rabbit dies, the game is over
        return -1

# Create a function that is called before the main routine starts, therefore begins as soon as the user opens the program
def restart():
    # Make user_name a global variable meaning that it can be changed if the game restart
    global user_name
    # Ask the user to enter their name and set this as the variable user_name
    user_name = input("Welcome to Virtual Pet! Please type your name here: ").strip().title()
    print()
    # Create a welcome message and give them information on how to use the program
    print("Hello, {}. Welcome to Virtual Pet!\nThis game allows you to look after your very own pet rabbit that you can feed and exercise.\nRemember: The weight of your rabbit must stay above 1.5kg and below 2.5kg otherwise they will die.".format(user_name))
    print()
    # Make rabbit_name a global variable meaning that it can be changed if the game restarts
    global rabbit_name
    # Ask the user to name their rabbit and set this as the variable rabbit_name
    rabbit_name = input("Please type what you would like to call your rabbit: ").strip().title()
    print("{} is a lovely name!".format(rabbit_name))
    print()
    # Make rabbit_weight a global variable meaning that it can be changed if the game restarts
    global rabbit_weight
    # Ask the user what they want their rabbit to weigh - this number must be between 1.5kg and 2.5kg
    # Call my float checking function to ensure that the weight of the rabbit is valid
    rabbit_weight = check_float("Please type the weight you want your rabbit to be. This number must be between 1.5 and 2.5", "This number is not between 1.5 and 2.5.", 1.5, 2.5)
    print()
    # Rabbit symbol, customised from https://kipkis.com/Make_a_Bunny_by_Typing_Characters_on_Your_Keyboard
    print("(\_/)        Perfect! Let's get started, {}!".format(user_name))
    print("(>.<)        Your pet rabbit's name is {}".format(rabbit_name))
    print('(")_(")      and they weigh {:.2f}kg!'.format(rabbit_weight))
    print()

# Main routine
restart()

while (True):
    # The main menu prints
    main_choice = main_menu()
    # If the user selects option 1 the feed function is called and will begin
    if main_choice == 1:
        rabbit_weight = feed()
        # If the rabbit dies (this is signified by -1), the restart function is called so the user can play again
        if rabbit_weight == -1:
            restart()
    # If the user selects option 2 the exercise function is called and will begin
    if main_choice == 2:
        rabbit_weight = exercise()
        # Once again, if the rabbit dies (which is signified by -1), the restart function is called so the user can play again
        if rabbit_weight == -1:
            restart()
    # If the user selects option 3 the current weight of their rabbit is printed
    if main_choice == 3:
        print("{} weighs {:.2f}kg.".format(rabbit_name, rabbit_weight))
        print()
    # If the user selects option 4 the game ends and the user receives a goodbye message
    if main_choice == 4:
        print("Goodbye, {}. I hope you enjoyed playing Virtual Pet! See you next time.".format(user_name))
        exit()
    # If the user selects option 5 the receive a help message
    if main_choice == 5:
        print("Welcome to Virtual Pet! \nThis game allows you to look after your very own pet rabbit that you can feed and exercise. \nThe main menu gives you options of what you can do with your rabbit! You could feed your rabbit, exercise your rabbit, check your rabbit's weight, end the game, ask for help or even restart. \nRemember: Your pet rabbit must stay between 1.5kg and 2.5kg otherwise it will die, so make sure to feed and exercise your rabbit regularly!\nHave fun playing!")
        print()
    # If the user selects option 6 the restart function is called so the user can restart the game
    if main_choice == 6:
        # Print some hyphens to show that a new game has started
        print("---------------------------------------------------")
        restart()
    input("Press any key and [enter] to continue: ")
    print()
