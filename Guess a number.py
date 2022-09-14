#Guess a number
import random
print("Welcome to the Number Gessing Game!\nI'm thinking of a number between 1 and 100")

answer = random.randint(1, 100)
print(f"Psss.. the answer is {answer}")

#global variables
EASY_TURNS = 10
HARD_TURNS = 5

def set_complexity():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def compare(guess, answer):
    if guess < answer:
        print("Too low")
        
    elif guess > answer:
        print("Too high")
        
    else:
        print(f"You got it, the number is {answer}")
        

def play_game():
    turns = set_complexity()
    
    # guess = int(input("Make a guess: "))
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
             
        turns -= 1
        
        guess = int(input("Make a guess: "))        
        compare(guess, answer) 
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
              
play_game()
