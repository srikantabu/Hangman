from string import ascii_lowercase
from Words import getRandomWord

def getNumAttempts():
    """Get inputted number of incorrect attempts for the game"""
    while True:
        numAttempts = input('How many incorrect attempts do you want? [1-25] ')
        try:
            numAttempts = int(numAttempts)
            if 1 <= numAttempts <= 25:
                return numAttempts
            else:
                print('{0} is not between 1 to 25'.format(numAttempts))
        except ValueError:
            print('{0} is not a number between 1 to 25'.format(numAttempts))

def getMinWordLength():
    """Get inputted minimum word length for the game"""
    while True:
        minWordLength = input('What minimum word length do you want [4-16] ')
        try:
            minWordLength = int(minWordLength)
            if 4 <= minWordLength <= 16:
                return minWordLength
            else:
                print('{0} is not between 4 to 16'.format(minWordLength))
        except ValueError:
            print('{0} is not a number between 4 to 16'.format(minWordLength))

def getDisplayWord(word, idxs):
    """Get the word suitable for display"""
    if len(word) != len(idxs):
        raise ValueError('Word length and indices length are not the same')
    displayedWord = ''.join([letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayedWord.strip()

def getNextLetter(remainingLetters):
    """Get inputted next letter"""
    if len(remainingLetters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        nextLetter = input('Choose the next letter ').lower()
        if len(nextLetter) != 1:
            print('Input only one letter')
        elif nextLetter not in  ascii_lowercase:
            print('{0} is not a letter'.format(nextLetter))
        elif nextLetter not in remainingLetters:
            print('{0} has been guessed before'.format(nextLetter))
        else:
            remainingLetters.remove(nextLetter)
            return nextLetter

def PlayHangman():
    """Play a game of hangman. At the end of the game, returns if the player wants to retry."""
    #Let player specify difficulty
    print('Starting a game of Hangman...')
    attemptsRemaining = getNumAttempts()
    minWordLength = getMinWordLength()
    #Randomly select a word
    print('Selecting a word...')
    word = getRandomWord(minWordLength)
    print()
    #Initialize game state variables
    idxs = [letter not in ascii_lowercase for letter in word]

    remainingLetters = set(ascii_lowercase)
    wrongLetters = []
    wordSolved = False
    #Main game loop
    while attemptsRemaining > 0 and not wordSolved:
        #Print current game state
        print('Word: {0}'.format(getDisplayWord(word, idxs)))
        print('Attempts remaining: {0}'.format(attemptsRemaining))
        print('Previous guesses: {0}'.format(' '.join(wrongLetters)))

        #Get player's next letter guess
        nextLetter = getNextLetter(remainingLetters)

        #Check if letter guess is in word
        if nextLetter in word:
            #Guessed correctly
            print('{0} is the word!'.format(nextLetter))

            #Reveal matching letters
            for i in range(len(word)):
                if word[i] == nextLetter:
                    idxs[i] = True
        else:
            #Guessed incorrectly
            print('{0} is NOT in the word'.format(nextLetter))

            #Decrement number of attempts left and append guess to wrongLetters
            attemptsRemaining -= 1
            wrongLetters.append(nextLetter)

        #Check if word is correctly wordSolved
        if False not in idxs:
            wordSolved = True
        print()
    #The game is over reveal the words
    print('The word is {0}'.format(word))

    #Notify player of victory or defeat
    if wordSolved:
        print('Congratulations!!You won!!')
    else:
        print('Next time okie!?')

    #Ask player if he/she wants to try again
    tryAgain = input('Would you like to try again? [y/n] ')
    return tryAgain.lower() == 'y'

if __name__ == '__main__':
    while PlayHangman():
        print()
