# Create a universal integer checking function
# Question and error allow it to be used in a range of situations
def check_int(question, error, low, high):
    valid = False
    while not valid:
        # Any question that needs a number
        number = input("{}: ".format(question))
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        # If an invalid input is made, the prompt is made again
        except ValueError:
            # The error that prints is customised to the question
            print(error)

# Create a universal float checking function
# Question and error allow it to be used in a range of situations
def check_float(question, error, low, high):
    valid = False
    while not valid:
        # Any question that needs a number
        number = input("{}: ".format(question))
        try:
            number = float(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        # If an invalid input is made, the prompt is made again
        except ValueError:
        # The error that prints is customised to the question
            print(error)

# Create a dictionary of different things eg. weight and exercise, that user can check about their rabbit
MAIN_DICT = {1: "feed", 2: "exercise", 3: "check weight", 4: "end game", 5: "help"}

# Create a dictionary with each food that the user can choose from
FOOD_DICT = {1: "kale", 2: "broccoli", 3: "apple"}

# Create a dictionary with each food and the number of kilograms it will add to the weight of the rabbit
FOOD_WEIGHT_DICT = {"kale": 0.3, "broccoli": 0.2, "apple": 0.4}

# Create a dictionary with each exercise that the user can choose from
EXERCISE_DICT = {1: "hopping", 2: "running", 3: "walking"}

# Create a dictionary with each exercise and the number of kilograms it will subtract to the weight of the rabbit
EXERCISE_WEIGHT_DICT = {'hopping': 0.3, 'running': 0.5, 'walking': 0.1}

# Create a function that prints the main menu
def main_menu():
    print("Please select an option from the menu below.")
    print("     1. Feed {}".format(rabbit_name))
    print("     2. Exercise {}".format(rabbit_name))
    print("     3. Check {}'s Weight".format(rabbit_name))
    print("     4. End Game")
    print("     5. Help")
    print("     6. Restart")
    print()

    # Ask the user to input the number that relates to the action they want to perform
    main_choice = check_int("Type a number from the list above. This number must be between 1 and 5", "This number is not between 1 and 6.", 1,6)
    # Return the user's choice
    return main_choice

# Create a function that will be called when the user selects option 1
def feed():
    # Print a menu with the food that the user can choose from
    print("Please choose a food to feed {}.".format(rabbit_name))
    print("     1. Kale (+ 0.3kg)")
    print("     2. Broccoli (+ 0.2kg)")
    print("     3. Apple (+ 0.4kg)")
    print()

    # Ask the user to input the number that relates to the food that they want to feed their rabbit
    food_choice = check_int("What food would you like to feed {}? Type a number between 1 and 3".format(rabbit_name), "This number is not between 1 and 3.", 1, 3)
    print()
    # Create a variable called food_weight that calls the number of kilograms that each food will add to the rabbit's original weight
    food_weight = FOOD_WEIGHT_DICT[FOOD_DICT[food_choice]]
    # Adds the number of kilograms that the selected food will add to the rabbit's original weight
    new_weight = rabbit_weight + food_weight

    # Print a message that tells the user the new weight of their rabbit
    print("Since {} ate {}, we will add {}kg to their weight.".format(rabbit_name, FOOD_DICT[food_choice], food_weight))
    print()

    check_weight(new_weight)
    # Return the new weight of the rabbit
    return new_weight

# Create a function that will be called when the user selects option 2
def exercise():
    # Print a menu with the exercise that the use can choose from
    print("Please choose an exercise for {}.".format(rabbit_name))
    print("     1. Hopping (- 0.3kg)")
    print("     2. Running (- 0.5kg)")
    print("     3. Walking (- 0.1kg)")
    print()

    # Ask the user to input the number that relates to the exercise that they want their rabbit to do
    exercise_choice = check_int("What exercise would you like {} to do? Type a number between 1 and 3".format(rabbit_name), "This number is not between 1 and 3.", 1, 3)
    # Create a variable called exercise_weight that calls the number of kilograms that each food will add to the rabbit's original weight
    exercise_weight = EXERCISE_WEIGHT_DICT[EXERCISE_DICT[exercise_choice]]
    # Create a new variable called new_weight that adds the number of kilograms that the selected food will add to the rabbit's original weight
    new_weight = rabbit_weight - exercise_weight

    # Print a message that tells the user the new weight of their rabbit
    print("Since {} did a {} exercise, we will take away {}kg from their weight.".format(rabbit_name, EXERCISE_DICT[exercise_choice], exercise_weight))
    print()

    check_weight(new_weight)
    # Return the rabbit's new weight
    return new_weight

# Create a function that check the rabbit's weight
def check_weight(new_weight):
    if 1.5 <= new_weight <= 2.5:
        continue_game = True
        print("{}'s weight is now {:.2f}!".format(rabbit_name, new_weight))
        print()
    else:
        if 1.5 > new_weight:
            print("I'm really sorry {}, but {} died because they were underweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {:.2f}kg.".format(user_name, rabbit_name, rabbit_name, new_weight))
        if 2.5 < new_weight:
            print("I'm really sorry {}, but {} died because they were overweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {:.2f}kg.".format(user_name, rabbit_name, rabbit_name, new_weight))
        # If the rabbit dies, exit the game
        exit()

# Create a function that is called before the main routine starts, therefore begins as soon as the user opens the program
def restart():
    # Ask the user to enter their name and set this as the variable user_name
    user_name = input("Welcome to Virtual Pet! Please type your name here: ").strip().capitalize()
    # Create a welcome message and give them information on how to use the program
    print("Hello, {}. Welcome to Virtual Pet! This game allows you to look after your very own pet rabbit that you can feed and exercise.".format(user_name))
    print()
    # Ask the user to name their rabbit and set this as the variable rabbit_name
    rabbit_name = input("Please type what you would like to call your rabbit: ").strip().capitalize()
    print("{} is a lovely name!".format(rabbit_name))
    print()
    # Ask the user what they want their rabbit to weigh - this number must be between 1.5kg and 2.5kg
    rabbit_weight = check_float("Please type the weight you want your rabbit to be. This number must be between 1.5 and 2.5", "This number is not between 1.5 and 2.5.", 1.5, 2.5)
    print()
    print("Perfect! Let's get started {}!".format(user_name))
    print()
    # Rabbit symbol customised from https://kipkis.com/Make_a_Bunny_by_Typing_Characters_on_Your_Keyboard
    print("(\_/)        Your pet rabbit's")
    print("(>.<)        name is {} and they".format(rabbit_name))
    print('(")_(")      weigh {}kg!'.format(rabbit_weight))
    print()


# Ask the user to input the number that relates to the action they want to perform
main_choice = input("Type a number from the list above. This number must be between 1 and 5: ")

if main_choice == 1:
    # Print a menu with the food that the user can choose from
    print("Please choose a food to feed {}.".format(rabbit_name))
    print("     1. Kale (+ 0.3kg)")
    print("     2. Broccoli (+ 0.2kg)")
    print("     3. Apple (+ 0.4kg)")

    # Ask the user to input the number that relates to the food that they want to feed their rabbit
    food_choice = input("What food would you like to feed {}. Type a number between 1 and 3: ".format(rabbit_name))
