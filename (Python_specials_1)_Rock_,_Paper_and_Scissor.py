import random
user_choice = int(input("Enter Your choice: Type 0 for rock, 1 for paper, 2 for scissors"))
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(computer_choice)
if computer_choice == user_choice:
    print("It's a Draw.")
elif computer_choice > user_choice:
    print("User lose.")
elif user_choice > computer_choice:
    print("User wins.")
elif computer_choice == 0 and user_choice == 2:
    print("User loses.")
elif user_choice == 0 and computer_choice == 2:
    print("User wins.")
