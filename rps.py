import random
import art

rock_paper = [art.rock, art.paper, art.scissors]
user_guess = int(input("rock for 0, paper for 1 , scissors for 2:"))
system_choice = random.randint(0,2)
print("your choice is:")
if user_guess >= 3 or user_guess <0:
    print("please select valid number")
else:  
    print(rock_paper[user_guess])
    print("the system choice is:")
    print(rock_paper[system_choice])
if user_guess == 0 and system_choice == 1:
    print("system wins the game")
elif user_guess == 1 and system_choice == 0:
    print("you wins the game")
elif user_guess == 0 and system_choice == 2:
    print("you wins the game")
elif user_guess == 2 and system_choice == 0:
    print("system wins the game")
elif user_guess == 1 and system_choice == 2:
    print("system wins the game")
elif user_guess == 2 and system_choice == 1:
    print("you wins the game")
else:
    print("Draw")  