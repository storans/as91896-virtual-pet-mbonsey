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

# Set rabbit_name to Kybe for testing purposes
rabbit_name = "Kybe"

# Set rabbit weight to 2.2 for testing purposes
rabbit_weight = 2.2

# Set user_name to Mads for testing purposes
user_name = "Mads"

# Print the main menu
print("Please select an option from the menu below.")
print("     1. Feed {}".format(rabbit_name))
print("     2. Exercise {}".format(rabbit_name))
print("     3. Check {}'s Weight".format(rabbit_name))
print("     4. End Game")
print("     5. Help")
print()

# Ask the user to input the number that relates to the action they want to perform
main_choice = input("Type a number from the list above. This number must be between 1 and 5: ")

if main_choice == 1:
    # Print a menu with the food that the user can choose from
    print("Please choose a food to feed {}.".format(rabbit_name))
    print("     1. Kale (+ 0.3kg)")
    print("     2. Broccoli (+ 0.2kg)")
    print("     3. Apple (+ 0.4kg)")
    print()
