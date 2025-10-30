import random
import art

head_tail = [art.head, art.tail]
user_guess = int(input("head for 0 , tail for 1:"))
system_choice = random.randint(0,1)
print("your choice is:")
print(head_tail[user_guess])
print("result is:")
print(head_tail[system_choice])
if user_guess == system_choice:
    print("you won")
else:
    print("you lost")