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
