# start of number game.
#based on https://inventwithpython.com/guess.py
import random

guessesTaken = 0
guessesLeft =  6

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
            print("That's not a number stupid")
        
        guessesTaken = guessesTaken + 1
        guessesLeft = guessesLeft - 1
   
        if guess < number:
            print('Your guess is too low.') 

        if guess > number and guess < 10:
            print('Your guess is too high.')
        
        if guess >= 11:
            print('Please use a number 1-10.')
        
        if guessesLeft <= 5 and guessesLeft != 0:
            print ('You have ' +  str(guessesLeft) + ' guesses left.')

        if guess == number:
            break
          
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')
        numberGuess()

    if guess != number:
        number = str(number)
        print('Nope. ' + number + ' was the number I was thinking of.' + "\n" + "\n" + 'Lets play again!')
        numberGuess()
numberGuess()
