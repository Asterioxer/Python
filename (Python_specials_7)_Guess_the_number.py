import random
First_Level_Attempts = 10
Second_Level_Attempts = 5
def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return First_Level_Attempts
    elif level_chosen =='hard':
        return Second_Level_Attempts
    else:
        return 
    
def check_input(chosen_number,answer,attempts):
    if chosen_number < answer:
        print("Your choice is too low!")
        return attempts - 1
    elif chosen_number > answer:
        print("Your guess is too high!")
        return attempts - 1
    else: 
        print(f"Your guess is right..... the answer was {answer}")
def game():
 print("Think of a number from 1 to 50.")
 answer = random.randint(1,50)
 level = input("Choose the type of difficulty")
 attempts = set_difficulty(level)
 if attempts!= First_Level_Attempts and attempts!= Second_Level_Attempts:
     print("You have entered wrong level of difficulty, please rectify the same and enter the proper input choice")
     return
 chosen_number = 0
 while chosen_number != answer:
  print(f"You have {attempts} remaining to choose numbers. ")
  chosen_number = int(input("Choose a number: "))
  attempts = check_input(chosen_number,answer,attempts)
  if attempts == 0:
      print("You are out of guesses... You lose!")
      return
  elif chosen_number != answer:
      print("Guess again")

game()


