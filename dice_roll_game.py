import random
random.random()

def dice_roll():
    return ('You rolled a: ')+ str(random.randint(1,6)))


user_input = ''

while user_input != 'Quit':
    user_input = input('Hi, this is the random dice roll game.\nTo roll the dice type ROLL.\nTo quit the game type QUIT.\nOk let\'s start: ')
    if user_input.lower() == 'roll':
        print(dice_roll())
    elif user_input.lower() == 'quit':
        print('Thank you for playing')
        break
    else:
        print('Invalid input')
    
