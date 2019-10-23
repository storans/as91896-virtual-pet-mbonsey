# Create a dictionary of different things eg. weight and exercise, that user can check their rabbit for
MAIN_DICT = {1: "feed", 2: "exercise", 3: "check weight", 4: "end game", 5: "help"}

# Create a dictionary with each food that the user can choose from
FOOD_DICT = {1: "kale", 2: "broccoli", 3: "apple"}

# Create a dictionary with each food and the number of kilograms it will add to the weight of the rabbit
FOOD_WEIGHT_DICT = {"kale": 0.3, "broccoli": 0.2, "apple": 0.4}

# Create a dictionary with each exercise that the user can choose from
EXERCISE_DICT = {1: "hopping", 2: "running", 3: "walking"}

# Create a dictionary with each exercise and the number of kilograms it will subtract to the weight of the rabbit
EXERCISE_WEIGHT_DICT = {'hopping': 0.3, 'running': 0.5, 'walking': 0.1}

# Ask the user to name their rabbit and set this as the variable rabbit_name
rabbit_name = input("Please type what you would like to call your rabbit here: ").strip().capitalize()
print()

# Set rabbit weight to 2.1 for testing purposes
rabbit_weight = 2.2

# Set user_name to Mads for testing purposes
user_name = "Mads"

print("Please select an option from the menu below.")
print("     1. Feed {}".format(rabbit_name))
print("     2. Exercise {}".format(rabbit_name))
print("     3. Check {}'s Weight".format(rabbit_name))
print("     4. End Game")
print("     5. Help")
print()

# Ask the user to input the number that relates to the action they want to perform
main_choice = int(input("Type a number from the list above. This number must be between 1 and 5: "))
print()

if main_choice == 1:
    # Print a menu with the food that the user can choose from
    print("Please choose a food to feed {}.".format(rabbit_name))
    print("     1. Kale (+ 0.3kg)")
    print("     2. Broccoli (+ 0.2kg)")
    print("     3. Apple (+ 0.4kg)")
    print()

    # Ask the user to input the number that relates to the food that they want to feed their rabbit
    food_choice = int(input("What food would you like to feed {}. Type a number between 1 and 3: ".format(rabbit_name)))
    print()
    # Create a variable called food_weight that calls the number of kilograms that each food will add to the rabbit's original weight
    food_weight = FOOD_WEIGHT_DICT[FOOD_DICT[food_choice]]
    # Create a new variable called new_weight that adds the number of kilograms that the selected food will add to the rabbit's original weight
    after_food_weight = rabbit_weight + food_weight

    # Print a message that tells the user the new weight of their rabbit
    print("Since {} ate {}, we will add {}kg to their weight.".format(rabbit_name, FOOD_DICT[food_choice], food_weight))
    print()

    if 1.5 <= after_food_weight <= 2.5:
        continue_game = True
        print("{}'s weight is now {.2f}!".format(rabbit_name, after_food_weight))
    else:
        if 1.5 > after_food_weight:
            print("I'm really sorry {}, but {} died because they were underweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {}kg.".format(user_name, rabbit_name, rabbit_name, after_food_weight))
        if 2.5 < after_food_weight:
            print("I'm really sorry {}, but {} died because they were overweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {}kg.".format(user_name, rabbit_name, rabbit_name, after_food_weight))
        continue_game = False

if main_choice == 2:
    # Print a menu with the exercise that the use can choose from
    print("Please choose an exercise for {}.".format(rabbit_name))
    print("     1. Hopping (- 0.3kg)")
    print("     2. Running (- 0.5kg)")
    print("     3. Walking (- 0.1kg)")
    print()

    # Ask the user to input the number that relates to the exercise that they want their rabbit to do
    exercise_choice = int(input("What exercise would you like {} to do.Type a number between 1 and 3: ".format(rabbit_name)))
    print()
    # Create a variable called exercise_weight that calls the number of kilograms that each food will add to the rabbit's original weight
    exercise_weight = EXERCISE_WEIGHT_DICT[EXERCISE_DICT[exercise_choice]]
    # Create a new variable called new_weight that adds the number of kilograms that the selected food will add to the rabbit's original weight
    after_exercise_weight = after_food_weight - exercise_weight

    # Print a message that tells the user the new weight of their rabbit
    print("Since {} did a {} exercise, we will take away {}kg from their weight.".format(rabbit_name, EXERCISE_DICT[exercise_choice], exercise_weight))
    print()

    if 1.5 <= after_exercise_weight <= 2.5:
        continue_game = True
        print("{}'s weight is now {.2f}!".format(rabbit_name, after_exercise_weight))
    else:
        if 1.5 > after_exercise_weight:
            print("I'm really sorry {}, but {} died because they were underweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {}kg.".format(user_name, rabbit_name, rabbit_name, after_exercise_weight))
        if 2.5 < new_weight:
            print("I'm really sorry {}, but {} died because they were overweight. To keep your rabbit alive, they must be between 1.5kg and 2.5kg and {} was {}kg.".format(user_name, rabbit_name, rabbit_name, after_exercise_weight))
        continue_game = False


