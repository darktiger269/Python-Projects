import random

def restart():
    # Setting Variables for Lower + Upper Bounds
    lower_bound = int(input('Select A Lower Bound Number: '))
    upper_bound = int(input('Select A Upper Bound Number: '))
    # Setting Random Number based on two different inputs

    while lower_bound >= upper_bound:
        print('Lower cannot be greater than upper. \n Please enter another number.')
        lower_bound = int(input('Select A Lower Bound Number: '))
        upper_bound = int(input('Select A Upper Bound Number: '))

    random_number = random.randint(lower_bound, upper_bound)
    user_choice = int(
        input('Please guess a number between ' + str(lower_bound) + ' and ' + str(upper_bound) + '\n Your Guess: '))

    while user_choice < lower_bound or user_choice > upper_bound:
        user_choice = int(
            input('Please guess a number between ' + str(lower_bound) + ' and ' + str(upper_bound) + '\n Your Guess: '))

    while user_choice != random_number:
        if user_choice > random_number:
            print('Please guess lower!')
            user_choice = int(input('Your number: '))

        if user_choice < random_number:
            print('Please guess higher!')
            user_choice = int(input('Your number: '))

        else:
            print('Damn mf. You guessed it correctly.')
            choice2 = input('Do you want to play again? yes/no ')
            if 'yes' in choice2:
                restart()
            if 'no' in choice2:
                print('Goodbye. Please restart the game manually if you would like to play again.')
# Setting Variables for Lower + Upper Bounds
lower_bound = int(input('Select A Lower Bound Number: '))
upper_bound = int(input('Select A Upper Bound Number: '))
# Setting Random Number based on two different inputs

while lower_bound >= upper_bound:
    print('Lower cannot be greater than upper. \n Please enter another number.')
    lower_bound = int(input('Select A Lower Bound Number: '))
    upper_bound = int(input('Select A Upper Bound Number: '))

random_number = random.randint(lower_bound, upper_bound)
user_choice = int(input('Please guess a number between ' + str(lower_bound) + ' and ' + str(upper_bound) + '\n Your Guess: '))

while user_choice < lower_bound or user_choice > upper_bound:
    user_choice = int(input('Please guess a number between ' + str(lower_bound) + ' and ' + str(upper_bound) + '\n Your Guess: '))

while user_choice != random_number:
    if user_choice > random_number:
        print('Please guess lower!')
        user_choice = int(input('Your number: '))

    if user_choice < random_number:
        print('Please guess higher!')
        user_choice = int(input('Your number: '))

    else:
        print('Damn mf. You guessed it correctly.')
        choice2 = input('Do you want to play again? yes/no ')
        if 'yes' in choice2:
            restart()
        if 'no' in choice2:
            print('Goodbye. Please restart the game manually if you would like to play again.')




