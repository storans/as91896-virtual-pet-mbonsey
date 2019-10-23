# Create a function that allows to check the float the user inputs
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

# user_name = input("Welcome to Virtual Pet! Please type your name here: ").strip().capitalize()
print()

# Create a welcome message and give them information on how to use the program
print("Hello, {} and welcome to Virtual Pet! This game allows you to look after your very own pet rabbit that you can feed and exercise.".format(user_name))
print()

# Ask the user to name their rabbit and set this as the variable rabbit_name
rabbit_name = input("Firstly, you need to decide on what you would like to call your pet rabbit. Type their name here: ").strip().capitalize()
print()
print("{} is such a lovely name!".format(rabbit_name))

# Ask the user to select a weight for their rabbit and set this as the variable rabbit_weight
rabbit_weight = float_check("Now you need to choose {}'s weight. Type a number between 1.5 and 2.5: ".format(rabbit_name, rabbit_name), "This number is not between 1.5 and 2.5. PLease type another number: ")
