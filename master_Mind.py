#!/bin/python3
# MasterMind
# by ICTROCN
# v1.02
# 15-8-2024
# Last mod by DevJan : added loop for replay
# Updated: colored guesses by typing color names + decoder feedback (NL)
#          ported from Methods.java -> decoder()
print("")
print("")
print("                              ==================")
print("                              === MasterMind ===")
print("                              ==================")

import random

COLORS = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange']


def generate_Code(length=4):
    return [random.choice(COLORS) for _ in range(length)]


def return_Code():
    secret_Code = generate_Code()
    return secret_Code


def adminLogin():
    password = "admin123"
    attempts = 5
    while attempts > 0:
        print("")
        print("")
        entered_Password = input("================== Enter admin password to view the secret code: =============")
        if entered_Password == password:
            return True
        else:
            attempts -= 1
            print("")
            print(f"Incorrect password. {attempts} attempts remaining.")
    return False


def login():
    if adminLogin():
        print("")
        print("")
        print("===========  Admin access granted. Starting game with admin access. =============")
        print(return_Code())
        return True
    else:
        print("")
        print("")
        print("===========  Admin access denied. Starting game without admin access. =============")
        return True


def mogelijke_kleuren():
    print("============================================================================================")
    print("============================================================================================")
    opties = ", ".join(COLORS)
    print(f"||||||||     Mogelijke kleuren: {opties}     |||||||||||||")
    print("============================================================================================")
    print("============================================================================================")


def colorChoose(naam):

    for kleur in COLORS:
        if kleur.lower() == naam.lower():
            return kleur
    return None


def get_Guess(length=4):
    guess = []
    for vak in range(length):
        while True:
            raw = input(f"Vak_{vak + 1} - kies een kleur ({', '.join(COLORS)}): ").strip()
            kleur = colorChoose(raw)
            if kleur is not None:
                print(f"  -> Vak_{vak + 1}: {kleur}")
                guess.append(kleur)
                break
            else:
                print(f"Ongeldige kleur. Kies een van: {', '.join(COLORS)}")
    return guess


def decoder(playerGuesses, correctColors):
    
    isWin = True
    checked = [False] * len(correctColors)

    for i in range(len(playerGuesses)):
        if playerGuesses[i] == correctColors[i]:
            print(f"Vak_{i + 1} is goed!")
        else:
            isWin = False
            found = False

            for j in range(len(correctColors)):
                if playerGuesses[i] == correctColors[j] and not checked[j]:
                    found = True
                    checked[j] = True
                    break

            if found:
                print(f"Vak_{i + 1} niet goed, maar kleur komt wel in de doosje.")
                print("============================================================================================")

            else:
                print(f"Vak_{i + 1} is niet goed!")
                print("============================================================================================")
    return isWin


def play_Mastermind():

    print("")
    print("")
    print("=============================================================================")
    print("                           Welcome to Mastermind!                            ")
    print("=============================================================================")
    print("")
    print("")
    mogelijke_kleuren()
    print("")
    print("Guess the 4-Color code by typing the color name for each Vak. You have 10 attempts.")
    print("")
    print("")
  
    attempts = 10
    secret_Code = return_Code()
    for attempt in range(1, attempts + 1):
        print(f"--- Poging {attempt} van {attempts} ---")
        guess = get_Guess(len(secret_Code))

        isWin = decoder(guess, secret_Code)

        if isWin:
            print(f"Congratulations! You guessed the code: {', '.join(secret_Code)}")
            return

        print("")

    print(f"Sorry, you've used all attempts. The correct code was: {', '.join(secret_Code)}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        print("")
        print("")
        if input("Do you want to login as admin to view the secret code ? (Y/N) ").upper() == 'Y':
            login()
            play_Mastermind()
        else:
            play_Mastermind()
        again = input("Play again (Y/N) ?").upper()