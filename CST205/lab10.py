"""
Lab #10: Strings
Pair Partners: Ashley Wallace & Brittany Mazza (Team #6)
"""

def hangman():
    word = "programming"
    word = word.upper()
    guessedLetters = ""
    incorrectGuesses = ""
    solvedWord = len(word) * "_"
    
    printInstructions()
    display("Word to solve:", solvedWord)
    print ""
    
    while len(incorrectGuesses) < 6 and not (solvedWord == word):
        guess = requestString("Enter your guess").upper()
        if not guess.isalpha() or not (len(guess) == 1):
            print "Enter a valid character."
            continue
        elif guess in guessedLetters:
            print "%s has already been guessed" % (guess)
            continue
        elif guess in word:
            solvedWord = solveWord(solvedWord, word, guess)           
            valid = "correct"
        else:
            incorrectGuesses = incorrectGuesses + guess
            valid = "incorrect"
        guessedLetters = guessedLetters + guess
        print "------------------------------------------------------------------"
        print "Your guess (%s) is %s!" % (guess, valid)
        display("Word so far:", solvedWord)
        display("Incorrect guesses:", incorrectGuesses)
        print "You have used %s of six guesses" % (len(incorrectGuesses))
    if len(incorrectGuesses) > 5:
        print "\n***You've lost!***\n"
    elif solvedWord == word:
        print "\n***You've won!***\n"
    
def display(title, stringToDisplay):
    print title
    for character in stringToDisplay:
        print character,
    print ""

def solveWord(wordInProgress, answer, guessLetter):
    newWord = ""
    for x in range(0, len(wordInProgress)):
        if answer[x] == guessLetter and wordInProgress[x] == '_':
            newWord = newWord + guessLetter
        else:
            newWord = newWord + wordInProgress[x]
    return newWord

def printInstructions():
    print "*******************************************************************"
    print "                      Welcome to hangman!"
    print " You will be given a set of blank values that make a word. Your "
    print " goal is to correctly guess each letter in the word. If you get"
    print " one wrong, a stick figure portion is added to the hangman and you"
    print " will have lost a point."
    print ""
    print " General guidelines:"
    print " * Enter a single letter for each guess."
    print " * You can have only 6 wrong guesses (2 legs, 2 arms, and 1 head)"
    print "*******************************************************************"
