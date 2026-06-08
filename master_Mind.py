#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("")
print("")
print("                              ==================")
print("                              === MasterMind ===")
print("                              ==================")

import random

def generate_Code(length=4):
    colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange']
     
    return [random.choice(colors) for _ in range(length)]
    
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

            
        
        
        

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)

def play_Mastermind():
    
    
    print("")
    print("")   
    print("Welcome to Mastermind!")
    print("")
    print("")
    print("Guess the 4-Color code. you can Choose between ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange']. You have 10 attempts.")
    print("")
    print("")
    secret_Code = return_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").strip()
            valid_Guess = len(guess) == 4 and all(c in "123456" for c in guess)
            if not valid_Guess:
                print("Invalid input. Enter 4 digits, each from 1 to 6.")


        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        print("")
        print("")
        if input("Do you want to login as admin to view the secret code ? (Y/N) ").upper() == 'Y':
            login()
            play_Mastermind()
            
        else:
            play_Mastermind()
    again  = input (f"Play again (Y/N) ?").upper()

