 
import random
import time
import os
import sys

words_list = [
    "jawbreaker",
    "jaywalk",
    "jazziest",
    "jazzy",
    "jelly",
    "jigsaw",
    "jinx",
    "jiujitsu",
    "jockey",
    "jogging",
    "joking",
    "jovial",
    "joyful",
    "juicy",
    "jukebox",
    "jumbo",
    "kayak",
    "kazoo",
    "keyhole",
    "khaki",
    "kilobyte",
    "larynx",
    "lengths",
    "lucky",
    "luxury",
    "lymph",
    "marquis",
    "matrix",
    "megahertz",
    "naphtha",
    "nightclub",
    "nowadays",
    "nymph",
    "onyx",
    "ovary",
    "oxidize"
]

def drawHangman(face=False, neck=False, body=False, left_hand=False, right_hand=False, left_leg=False, right_leg=False):
    for row in range(10):
        if row == 0:
                for column in range(20):
                    if column >= 3:
                        if column == 19:
                            print("_")
                        else:
                            print("_", end="")
                    else:
                        print(" ",end="")
        
        elif face == True and row == 1:
            for column in range(20):
                if column == 0:
                    print(" ",end="")
                elif column == 1:
                    print("_",end="")
                elif column == 2:
                    print("|", end="")
                elif column == 3:
                    print("_", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")
                    
        elif face == True and row == 2:
            for column in range(20):
                if column == 0 or column == 4:
                    print("|", end="")
                elif column == 1 or column == 3: 
                    print(" ", end="")
                elif column == 2:
                    print("_", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")
       
        elif neck == True and row == 3:
            for column in range(20):
                if column == 2:
                    print("|", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ",end="")

        elif left_hand == True and row == 4:
            for column in range(20):
                if column == 0:
                    print("/", end="")
                elif column == 1:
                    print(" ",end="")
                elif column == 2:
                    print("|", end="")
                elif column == 3:
                    print(" ",end="")
                elif right_hand == True and column == 4:
                    print("\\", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        
        elif body == True and row == 5:
            for column in range(20):
                if column == 2:
                    print("|", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ",end="")
  
        elif left_leg and row == 6:
            for column in range(20):
                if column == 0:
                    print("/", end="")
                elif column == 1:
                    print(" ",end="")
                elif column == 3:
                    print(" ",end="")
                    
                elif right_leg and column == 4:
                    print("\\", end="")
                elif column == 19:
                    print("|")
                else:
                    print(" ", end="")

        elif row == 9:
            for column in range(20):
                if column <= 10:
                    print(" ", end="")
                elif column == 19:
                    print("-")
                else:
                    print("-", end="")
        else:
            for column in range(20):
                if column == 19:
                    print("|")
                else:
                    print(" ", end="")  

def computerSelect():
    word = random.choice(words_list)
    return word.lower()

def playerSecretWord(repeatText = None):
    question = repeatText if repeatText is not None else "Enter your secret word.\n"
    word = input(question)
    if type(word) == str and len(word) >= 3:
        return word.lower()
    else:
        return playerSecretWord("Please make it atleast three letters! Try again.\n")

def drawGuessedLetters(guessed_letters):
    print("Word: ", end="")
    for letter in guessed_letters:
        print(letter, end="  ")
    print("\n")

def checkGuess(letter, phrase_letters):
    guess = False
    if letter in phrase_letters:
        guess = True
    return guess

def fillBlanks(letter, phrase_letters, guessed_letters):
    indices = [i for i, el in enumerate(phrase_letters) if el == letter]
    for index in indices:
        guessed_letters[index] = letter
    return guessed_letters

def guessLetter(repeatText = None):
    question = repeatText if repeatText is not None else "What's your guess?\n"
    word = input(question)
    if type(word) == str and len(word) == 1:
        return word.lower()
    else:
        return guessLetter("One letter at a time! Tty again.\n")
    
def ShowFaildAttempts(fails):
    print("Failed Attempts: ", end="")
    for miss in fails:
        print(miss, end=",")
    print("\n")


def drawHangmanBasedOnWrongGuessed(committed_mistakes):
    if committed_mistakes == 0:
        drawHangman(False, False, False, False, False, False, False)
    if committed_mistakes == 1:
        drawHangman(True, False, False, False, False, False, False)
    if committed_mistakes == 2:
        drawHangman(True, True, False, False, False, False, False)
    if committed_mistakes == 3:
        drawHangman(True, True, True, False, False, False, False)
    if committed_mistakes == 4:
        drawHangman(True, True, True, True, False, False, False)
    if committed_mistakes == 5:
        drawHangman(True, True, True, True, True, False, False)
    if committed_mistakes == 6:
        drawHangman(True, True, True, True, True, True, False)
    if committed_mistakes == 7:
        drawHangman(True, True, True, True, True, True, True)

def gameMode():
    question  = "Type your game option?\n\n"
    option = "1) One Player Mode\n2) Two Player Mode\n\n"
    game_type = input(question + option)
    if type(game_type) == str and game_type == "1" or game_type == "2":
        return int(game_type)
    else:
        gameMode()      

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

def clearScreen():
    platform = get_platform()
    if platform == "Windows": 
        os.system("cls")
    else:
        os.system("clear")

def startGame():

    game_type = gameMode()

    phrase= ""
    if game_type == 1:
        phrase = computerSelect()

    else:
        phrase = playerSecretWord()
        
    phrase_letters = [char for char in phrase]
    guessed_letters = ["__" for el in phrase_letters ]
    committed_mistakes = 0
    already_guessed_letters = []
    missed_letters = []

    clearScreen()
    no_win = True


    while(committed_mistakes < 7 and no_win):
        
        drawHangmanBasedOnWrongGuessed(committed_mistakes)

        drawGuessedLetters(guessed_letters)

        if len(missed_letters) > 0:
            ShowFaildAttempts(missed_letters)

        guessed_letter = guessLetter()
        
        if guessed_letter in already_guessed_letters:
            print("You already guessed that letter, try something else!")
            time.sleep(1)
            clearScreen()
            continue
        else:
            already_guessed_letters.append(guessed_letter)
       
        guessed = checkGuess(guessed_letter, phrase_letters)

        if guessed == True:
            guessed_letters = fillBlanks(guessed_letter, phrase_letters, guessed_letters)
            print("Nice Guess!")

            if guessed_letters == phrase_letters:
                no_win = False


        else:
            committed_mistakes += 1
            missed_letters.append(guessed_letter)
            print("Opps!")

        time.sleep(1)
        clearScreen()
    
    if no_win == False:
            drawGuessedLetters(guessed_letters)
            print("You Won! Great Job!")
    
    if committed_mistakes == 7:
        drawHangmanBasedOnWrongGuessed(committed_mistakes)
        print("Oops, you lost. Better luck next time!")
        print("The word was:- ", phrase)


startGame()
