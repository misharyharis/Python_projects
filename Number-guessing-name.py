import random


print("Welcome to the Number Guessing Game!")
print("Iam thinking of a number between 1 and 100.")
mode=input("Choose a difficulty. Type 'easy' or 'hard': ")
user_guess=int(input("Make a guess: "))

def number():
  number=random.randint(1,100)
  return number

def check_guess(user_guess,number):
  if user_guess<number:
    print("Too Low")
    print("Guess again")
  elif user_guess>number:
    print("Too High")
    print("Guess again")
  elif user_guess==number:
    print("You Got it")

def easy_mode():
  #global number
  numbers=number()
  print(numbers)
  for i in range(10):
    user_guess=int(input("Make a guess: "))
    check_guess(user_guess,numbers)
    if user_guess==numbers:
      break
    print(f"You have {9-i} attempts remaining to guess the number.")
    if i==10:
      print("You've run out of guesses, you lose.") 

def hard_mode():
  #global number
  numbers=number()
  print(numbers)
  for i in range(5):
    user_guess=int(input("Make a guess: "))
    check_guess(user_guess,numbers)
    if user_guess==numbers:
      break
    print(f"You have {4-i} attempts remaining to guess the number.")
    if i==5:
      print("You've run out of guesses, you lose.")

if mode=="easy":
  easy_mode()
  
elif mode=="hard":
  hard_mode()
  
else:
  print("Invalid Input")