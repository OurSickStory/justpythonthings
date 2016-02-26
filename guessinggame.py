#start of guessing number game.
#http://www.pythontutor.com/visualize.html#mode=display run this through here to get a great step by step!
#based on https://inventwithpython.com/guess.py
#final version. Look through the Commits to see the progress.
#you can play with it here; http://sobieski.codes/guess/

import random

def numberGuess():
    guessesTaken = 0
    guessesLeft =  6
    number = random.randint(1, 10)
    print('I am thinking of a number between 1 and 10.' + "\n"  + 'Can you guess the number?')
    print('You have 6 guesses.')

    while guessesTaken < 6:
        guess = input("Your guess:")

        try:
            guess = int(guess)
        except ValueError:
            print("That's not a number stupid.")
            continue

        guessesTaken = guessesTaken + 1
        guessesLeft = guessesLeft - 1

        if guess < number:
            print('Your guess is too low.') 

        if guess > number and guess <= 10:
            print('Your guess is too high.')

        if guess > 10:
            print('Please use a number 1-10.')
            continue

        if guessesLeft <= 5 and guessesLeft != 0 and guess != number:
            print ('You have ' +  str(guessesLeft) + ' guesses left.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job! You guessed my number in ' + guessesTaken + ' guesses!' + "\n" + "\n" + 'Lets play again!')
        numberGuess()

    if guess != number:
        number = str(number)
        print('Nope. ' + number + ' was the number I was thinking of.' + "\n" + "\n" + 'Lets play again!')
        numberGuess()

numberGuess()
