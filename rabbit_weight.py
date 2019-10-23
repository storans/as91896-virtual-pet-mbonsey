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

# Ask the user what they want their rabbit to weigh - this number must be between 1.5kg and 2.5kg
rabbit_weight = check_float("Please type the weight you want your rabbit to be. This number must be between 1.5 and 2.5", "This number is not between 1.5 and 2.5.", 1.5, 2.5)
