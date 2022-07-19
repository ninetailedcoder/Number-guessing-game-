# Getting the random import
import random
# Generates random number to guess
number = random.randint(1,10)
# Additional instructions for user
print('If you want to end the game type [q]')
# Starts the game loop
while True:
    guess=input('Whats your guess?: ')
    # Terminates game early if user chooses to do so
    if guess == "q":
        print('Thanks for playing')
        break
    # Stops game is users guess is correct
    elif int(guess) == number:
        print('Congrats! you got it!')
        break
