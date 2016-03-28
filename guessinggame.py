#start of guessing number game.
#http://www.pythontutor.com/visualize.html#mode=display run this through here to get a great step by step!
#based on https://inventwithpython.com/guess.py
#final version. Look through the Commits to see the progress.
#you can play with it here; http://sobieski.codes/guess/

import random  #imports random

def numberGuess():  #defines the game to start, and loop.
    guessesTaken = 0  #how many guesses you've taken.
    guessesLeft =  ""  #how many guesses you have left.
    maxnumber = "" #blank input to use later
    maxnumber = input("What is the max number you\'d like to guess from?:") #has you pick your max number
    maxnumber = int(maxnumber) #makes sure its a number
    number = random.randint(1, maxnumber)  #picks the random number using the imported random
    guessesLeft = input("How many guesses would you like to have?:") #how many guesses you'd like
    guessesLeft = int(guessesLeft) #make sure its a number..
    if guessesLeft >= maxnumber: #makes sure its a realistic number...
        print('Please use a realistic number..')
        numberGuess() #you should never do this line.
    else:
        pass
    print('I\'m guessing of a number between 1 and {}'.format(maxnumber))
    while guessesTaken < guessesLeft:   #the while loop, while guesses is less then 6 start ->
        guess = input("Your guess:") #your input line.

        try:  #the try line.
            guess = int(guess) #checks to make sure your input is an integer (whole DIGIT, and only a digit)
        except ValueError: #if not catch the error
            print("That's not a number stupid.") #print the error
            continue #continue with the loop, obviously starts back from the start of the game

        guessesTaken = guessesTaken + 1 #if passes as a number, add a guess taken
        guessesLeft = guessesLeft - 1 #if pass remove a guess left

        if guess < number:  #if your guess is lower then the number picked
            print('Your guess is too low.')

        if guess > number and guess <= maxnumber:  #if your guess is higher then the number picked but lower then 11
            print('Your guess is too high.')

        if guess > maxnumber: #if your guess is higher then 10, and continue so you don't lose a guess.
            print('Please use a number 1-{}.'.format(maxnumber))
            continue

        if guessesLeft <= maxnumber and guessesLeft != 0 and guess != number: #if guesses left is 5 or less, but not zero and
            print ('You have {} guesses left.'.format(guessesLeft))

        if guess == number: #if guess is the number picked, break the while loop.
            break

    if guess == number:  #defines what happens after the while loop is broken.
        print('Good job! You guessed my number in {} tries.\nLets play again!\n'.format(guessesTaken))
        numberGuess() #you should never do this line.

    if guess != number: #after guesses is 0 and guess doesn't match the number ->
        print('Nope. The number I was thinking of was {}.\nLets play again!\n'.format(number))
        numberGuess() #you should never do this line.

numberGuess()

