'''import random moduel'''
import random

'''need user number to determine the guessing range'''
top_of_range = input("Type a number: ")

'''check if user range is a digit and convert script to integer to be read as a number'''
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    '''range needs to be larger than 0 and also a number in general'''
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

'''random number picked between 0 and user range with a guess counter'''    
random_number = random.randint(0, top_of_range)
guesses = 0

'''above should be working and TRUE while user is guessing 1 by 1 and turn digit guess script to integer. CONTINUE to say guess needs to be a number if it isn't'''
while True:
    guesses += 1
    user_guess = input ("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    '''if user guess is right then congratulate and end game'''
    if user_guess == random_number:
        print("You got it!")
        break
        '''use elif to combine 2 if else and the random number is not equal so check greater and then lesser'''
    elif user_guess > random_number:
            print("You were above the number!")
    else:
        print("You were below the number!")

'''show guess counter variable'''
print("You got it in", guesses, "guesses.")
