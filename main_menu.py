# Create a dictionary of different things eg. weight and exercise, that user can check their rabbit for
MAIN_DICT = {1: "check weight", 2: "feed", 3: "exercise", 4: "help", 5: "end game"}

# Main menu (customised from: https://extr3metech.wordpress.com/2014/09/14/simple-text-menu-in-python/)
def print_menu():
    print("1. Check Weight")
    print("2. Feed")
    print("3. Exercise")
    print("4. Help")
    print("5. End Game")

loop = True

# This while loop will continue until loop = False
while loop:
    print_menu()
    main_choice = input("Select a choice from the menu above. Type a number between 1 and 5: ")

    if main_choice==1:
        print("{} weighs {}kg.".format(rabbit_name, rabbit_weight))
    elif main_choice==2:
        def print_menu():
            print("1. Kale")
            print("2. Broccoli")
            print("3. Apple")
        loop = True
        # This while loop will continue until loop = False
        while loop:
            print_menu()
            food_choice = input("Select a food that you would like to feed {}. Type a number between 1 and 3: ".format(rabbit_name))
            new_weight = rabbit_weight +
            if food_choice==1:
                print("We have added 0.1kg to the weight of {} after he ate a piece of kale. {} now weighs {}kg.".format(rabbit_name, rabbit_name, ))



        ## You can add your code or functions here
    elif choice==3:
        print "Menu 3 has been selected"
        ## You can add your code or functions here
    elif choice==4:
        print "Menu 4 has been selected"
        ## You can add your code or functions here
    elif choice==5:
        print "Menu 5 has been selected"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")

