"""

--Problem 4 - The Game--
Now you will implement the function hangman, which takes one parameter - the secretWord the user 
is to guess. This starts up an interactive game of Hangman between the user and the computer. Be 
sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and 
getAvailableLetters, that you've defined in the previous part.

There are four important pieces of information you may wish to store:

secretWord: The word to guess.

lettersGuessed: The letters that have been guessed so far.

mistakesMade: The number of incorrect guesses made so far.

availableLetters: The letters that may still be guessed. Every time a player guesses a letter, 
the guessed letter must be removed from availableLetters (and if they guess a letter that is not 
in availableLetters, you should print a message telling them they've already guessed that - so 
try again!).

"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("Welcome to the game, Hangman!")
    print ("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = ''
    guessesLeft = 8
    print ("------------")
    while True:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print ("------------")
        if guessesLeft <= 0:
            print ("Sorry, You've ran out of guesses. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations! You've won!")
            break
