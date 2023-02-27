'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

import random

words = ["name", "swift", "java", "python", "yes"] # set of random words
tries = 6 # set number of tries
usedLetters = [] # letters used
answerLetters = [] # correct letters entered by user
selectedWord = random.choice(words)
correctLetters = [] # the correct answer of letters
inpAns = "" # initialiser for terminal input

for index in range(len(selectedWord)):    # Correct letter setup
    answerLetters.append("_")
    correctLetters.append(selectedWord[index])


while tries > 0:
    usedLettersDisplay = ""  
    answerLettersDisplay = ""
    for usedLetter in usedLetters:
        usedLettersDisplay= usedLettersDisplay + " " + usedLetter

    for index in range(len(selectedWord)):
        answerLettersDisplay = answerLettersDisplay + " " + answerLetters[index]

    print("\nYou have " + str(tries) + " tries left." + 
          "\nUsed letters: "+ str(usedLettersDisplay) +
          "\nWord: " + str(answerLettersDisplay))
    inpAns = input("Enter a letter: ")  # user enters a letter
    
    index = 0
    usedLetters.append(inpAns)
    for correctLetter in correctLetters:
    
        if inpAns == correctLetter:
           
            answerLetters[index] = inpAns
        index+=1
    if correctLetters == answerLetters: # if all correct the player is congratulated and the loop breaks
        print("Congratulations you have guessed the correct letters")
        break      
    
    tries = tries - 1   # try decrementing
    if tries == 0: # game over when tries runs out
        print("you lose")
       




