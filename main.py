from art import logo
print(logo)
from random import randint
#import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0
#Function to check user input against the answer
def check_answer(guess, answer, turns):
  """checks answer against guess. returns the number of turns remaining"""
  if guess > answer:
    print(f"Too high")
    return turns - 1
  elif guess < answer:
    print(f"Too low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}!")
    play_again = input("Would you like to play again? Type 'y' for yes, 'n' for no.: ")
    if play_again == "y":
      #clear()
      game()
    else:
      return

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level =="hard":
    return HARD_LEVEL_TURNS

def game(): 
  #choose a random number (1-100)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  #print(f"Psssst, the correct answer is {answer}")
  
  turns = set_difficulty()
  
  #let the user guess a number
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose")
      play_again = input("Would you like to play again? Type 'y' for yes, 'n' for no.: ")
      if play_again == "y":
        #clear()
        game()
      else:
        return
        
game()
#random number needs to pass through easy/hard functions and let user know how many guess are left and the direction they need to go

#repeat until they either run out of turns or guess correctly



#def easy():
#  guess = input("You have 10 attempts remaining to guess a number between 1 - 100: \n")
#  total_guess = guess
# total_guess = "10"
#  guess = int(input("Make a guess: "))
#  if guess != answer:
#    total_guess - 1
#    print(f"you have {guess} guesses remaining, choose again")
    
  

#def hard():
#  print("You have 5 attempts remaining to guess the number")

#print("Welcome to the Number Guessing Game!")
#difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
#if difficulty == "easy":
#  easy()
#else:
#  hard()


