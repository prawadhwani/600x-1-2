# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    for char in secretWord:
        if char in lettersGuessed:
            word += char
        else:
            word += '_ '
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = string.ascii_lowercase
    for char in lettersGuessed:
        letters = letters.replace(char, "")
    return letters


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
    print('Welcome to the game Hangman! \n'+'I am thinking of a word that is ' + str(len(secretWord)) +' letters long')
    guess = False
    guessNumber = 8
    lettersGuessed = []
    while(not guess or guessNumber>0):
        print('-----------' + '\n' + 'You have '+str(guessNumber)+' guesses left')
        #print('You have '+str(guessNumber)+' guesses left')
        guessNumber -= 1
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        letterInput = raw_input('Please guess a letter: ')
        letterInputInLower = letterInput.lower()

        if(letterInputInLower not in lettersGuessed):
            lettersGuessed += letterInputInLower
            if(letterInputInLower not in secretWord):
                print('Oops! That letter is not in my word: '+ getGuessedWord(secretWord, lettersGuessed))
            else:
                guessNumber += 1
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))

        else:
            print('Oops! You\'ve already guessed that letter:' + str(getGuessedWord(secretWord, lettersGuessed)))
            guessNumber += 1
        
        if(isWordGuessed(secretWord, lettersGuessed)):
            guess = True
            print('-----------')
            print('Congratulations, you won!')
            break
        if(guessNumber == 0):
            print('-----------')
            print('Sorry, you ran out of guesses. The word was ' + str(secretWord))
            break


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'zzz'
hangman(secretWord)
